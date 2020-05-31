from os import path

from restfulpy.testing import ApplicableTestCase

from mycards import Mycards


HERE = path.abspath(path.dirname(__file__))
DATA_DIRECTORY = path.abspath(path.join(HERE, '../data'))


class LocalApplicationTestCase(ApplicableTestCase):
    __application_factory__ = Mycards
    __story_directory__ = path.join(DATA_DIRECTORY, 'stories')
    __api_documentation_directory__ = path.join(DATA_DIRECTORY, 'markdown')

    def login(self, email, password, url='/apiv1/tokens', verb='CREATE'):
        super().login(
            form=dict(email=email, password=password),
            url=url,
            verb=verb
        )

