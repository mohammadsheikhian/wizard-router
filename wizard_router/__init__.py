import functools
from os.path import dirname

from nanohttp import settings
from restfulpy import Application
from sqlalchemy_media import StoreManager, FileSystemStore

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

    @classmethod
    def initialize_orm(cls, engine=None):
        StoreManager.register(
            'fs',
            functools.partial(
                FileSystemStore,
                settings.storage.local_directory,
                base_url=settings.storage.base_url,
            ),
            default=True
        )
        super().initialize_orm(cls, engine)


wizard_router = WizardRouter()
