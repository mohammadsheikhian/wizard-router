import functools
from os.path import dirname

from nanohttp import settings
from restfulpy import Application

from .controllers.root import Root



__version__ = '0.1.0'


class WizardRouter(Application):
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/wizard_router_dev
        test_url: postgresql://postgres:postgres@localhost/wizard_router_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres

      migration:
        directory: %(root_path)s/migration
        ini: %(root_path)s/alembic.ini

      storage:
        local_directory: %(root_path)s/data/assets
        base_url: http://localhost:8080/assets

   '''

    def __init__(self, application_name='wizard_router', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=dirname(__file__),
            version=__version__
        )

wizard_router = WizardRouter()

