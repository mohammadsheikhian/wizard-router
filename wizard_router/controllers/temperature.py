import os
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
            temperatures['gpu'] = process.stdout.decode()

        except:
            pass

        try:
            process = subprocess.run(
                'cat /sys/class/thermal/thermal_zone0/temp'.split(),
                stdout=subprocess.PIPE
            )
            temperature = int(process.stdout.decode()) / 1000
            temperatures['gpu'] = temperature

        except:
            pass

        return temperatures

