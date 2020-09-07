from nanohttp import json
from restfulpy.controllers import RootController, RestController

import wizard_router
from .temperature import TemperatureController
from .openvpn import OpenVPNController
from .openconnect import OpenConnectController


class Apiv1(RestController):

    temperatures = TemperatureController()
    openvpns = OpenVPNController()
    openconnects = OpenConnectController()

    @json
    def version(self):
        return dict(version=wizard_router.__version__)


class Root(RootController):
    apiv1 = Apiv1()
