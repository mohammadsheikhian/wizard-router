from os.path import abspath, dirname, join

from nanohttp import json
from restfulpy.controllers import RootController, RestController

import wizard_router


here = abspath(dirname(__file__))
attachment_storage = abspath(join(here, '../..', 'data/assets'))


class Apiv1(RestController):

    @json
    def version(self):
        return dict(version=wizard_router.__version__)


class Root(RootController):
    apiv1 = Apiv1()

