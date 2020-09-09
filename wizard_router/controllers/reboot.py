import re
import subprocess

from nanohttp import RestController, json


class RebootController(RestController):

    @json(prevent_form=True)
    def get(self):
        try:
            process = subprocess.run(
                'sudo reboot'.split(),
                stdout=subprocess.PIPE
            )
            ping['ping'] = process.stdout.decode()

        except:
            pass

        return {}
