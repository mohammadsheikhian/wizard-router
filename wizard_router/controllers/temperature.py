import subprocess

from nanohttp import RestController, json


class TemperatureController(RestController):

    @json(prevent_empty_form=True)
    def get(self):
        temperatures = dict(
            cpu='0',
            gpu='0',
        )

        try:
            process = subprocess.Popen(
                'cpu-temperature'.split(),
                stdout=subprocess.PIPE,
                shell=True,
                executable='/bin/bash',
            )
            output, error = process.communicate()
            output = output.decode()
            temperatures['cpu'] = output if output != '' else '0'

        except:
            pass

        try:
            process = subprocess.Popen(
                'gpu-temperature'.split(),
                stdout=subprocess.PIPE,
                shell=True,
                executable='/bin/bash',
            )
            output, error = process.communicate()
            output = output.decode()
            temperatures['gpu'] = output if output != '' else '0'

        except:
            pass

        return temperatures

