import re
import subprocess

from nanohttp import RestController, json


class TemperatureController(RestController):

    @json(prevent_form=True)
    def get(self):
        temperatures = dict(
            cpu='0',
            gpu='0',
        )

        try:
            process = subprocess.run(
                'vcgencmd measure_temp'.split(),
                stdout=subprocess.PIPE
            )
            stdout = process.stdout.decode()
            temperatures['gpu'] = re.findall('\d*[.]*\d', stdout)[0]

        except:
            pass

        try:
            process = subprocess.run(
                'cat /sys/class/thermal/thermal_zone0/temp'.split(),
                stdout=subprocess.PIPE
            )
            temperature = int(process.stdout.decode()) / 1000
            temperatures['cpu'] = temperature

        except:
            pass

        return temperatures

