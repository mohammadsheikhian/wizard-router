import re
import subprocess

from nanohttp import RestController, json


class PingController(RestController):

    @json(prevent_form=True)
    def get(self):
        ping = dict(
            ping='',
        )

        try:
            process = subprocess.run(
                'ping -c 4 8.8.8.8'.split(),
                stdout=subprocess.PIPE
            )
            ping['ping'] = process.stdout.decode()

        except:
            pass

        return ping

