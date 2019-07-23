from os.path import abspath, dirname, join

from nanohttp import json
from restfulpy.controllers import RootController, RestController

import mycards
from .card import CardController


here = abspath(dirname(__file__))
attachment_storage = abspath(join(here, '../..', 'data/assets'))


class Apiv1(RestController):

    cards = CardController()

    @json
    def version(self):
        return dict(version=mycards.__version__)


class Root(RootController):
    apiv1 = Apiv1()

