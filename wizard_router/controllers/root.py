import socket

from nanohttp import json, html
from restfulpy.controllers import RootController, RestController

import wizard_router
from .temperature import TemperatureController
from .openvpn import OpenVPNController
from .openconnect import OpenConnectController
from .ping import PingController
from .reboot import RebootController
from ..templating import template


class Apiv1(RestController):

    temperatures = TemperatureController()
    openvpns = OpenVPNController()
    openconnects = OpenConnectController()
    pings = PingController()
    reboots = RebootController()

    @json
    def version(self):
        return dict(version=wizard_router.__version__)


class Root(RootController):
    apiv1 = Apiv1()

    @template('index.mak')
    def index(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return dict(
            ip=ip,
        )

