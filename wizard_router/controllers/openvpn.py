import os

from nanohttp import RestController, json


class OpenVPNController(RestController):

    @json(prevent_form=True)
    def status(self):
        open_vpn = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system('systemctl is-active --quiet mohammad-openvpn')
            open_vpn['returnCode'] = status
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_vpn['returnCode'] = -1
            open_vpn['status'] = 'unknown'
            open_vpn['exceptionMessage'] = exp

        return open_vpn

    @json(prevent_form=True)
    def restart(self):
        open_vpn = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system('systemctl restart --quiet mohammad-openvpn')
            open_vpn['returnCode'] = status

            status = os.system('systemctl is-active --quiet mohammad-openvpn')
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_vpn['returnCode'] = -1
            open_vpn['status'] = 'unknown'
            open_vpn['exceptionMessage'] = exp

        return open_vpn

    @json(prevent_form=True)
    def stop(self):
        open_vpn = dict(
            status='active',
            returnCode=0,
            exceptionMessage=''
        )

        try:
            status = os.system('systemctl stop --quiet mohammad-openvpn')
            open_vpn['returnCode'] = status

            status = os.system('systemctl is-active --quiet mohammad-openvpn')
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except Exception as exp:
            open_vpn['returnCode'] = -1
            open_vpn['status'] = 'unknown'
            open_vpn['exceptionMessage'] = exp

        return open_vpn


