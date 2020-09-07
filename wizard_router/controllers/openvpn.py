import os

from nanohttp import RestController, json


class OpenVPNController(RestController):

    @json(prevent_form=True)
    def status(self):
        open_vpn= dict(
            status='active',
        )

        try:
            status = os.system('systemctl is-active --quiet mohammad-openvpn')
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except:
            pass

        return open_vpn

    @json(prevent_form=True)
    def reset(self):
        open_vpn = dict(
            status='active',
        )

        try:
            status = os.system('systemctl reset --quiet mohammad-openvpn')
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except:
            pass

        return open_vpn

    @json(prevent_form=True)
    def stop(self):
        open_vpn = dict(
            status='in-active',
        )

        try:
            status = os.system('systemctl stop --quiet mohammad-openvpn')
            open_vpn['status'] = 'active' if status == 0 else 'in-active'

        except:
            pass

        return open_vpn


