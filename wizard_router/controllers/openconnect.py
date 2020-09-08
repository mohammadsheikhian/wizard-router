import os

from nanohttp import RestController, json


class OpenConnectController(RestController):

    @json(prevent_form=True)
    def status(self):
        open_connect = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system(
                'systemctl is-active --quiet mohammad-openconnect'
            )
            open_connect['returnCode'] = status
            open_connect['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_connect['returnCode'] = -1
            open_connect['status'] = 'unknown'
            open_connect['exceptionMessage'] = exp

        return open_connect

    @json(prevent_form=True)
    def restart(self):
        open_connect = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system(
                'systemctl restart --quiet mohammad-openconnect'
            )
            open_connect['returnCode'] = status

            status = os.system(
                'systemctl is-active --quiet mohammad-openconnect'
            )
            open_connect['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_connect['returnCode'] = -1
            open_connect['status'] = 'unknown'
            open_connect['exceptionMessage'] = exp

        return open_connect

    @json(prevent_form=True)
    def stop(self):
        open_connect = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system('systemctl stop --quiet mohammad-openconnect')
            open_connect['returnCode'] = status

            status = os.system(
                'systemctl is-active --quiet mohammad-openconnect'
            )
            open_connect['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_connect['returnCode'] = -1
            open_connect['status'] = 'unknown'
            open_connect['exceptionMessage'] = exp

        return open_connect
