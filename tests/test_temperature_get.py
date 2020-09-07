from bddrest import status, response

from .helpers import LocalApplicationTestCase


class TestTemperature(LocalApplicationTestCase):

    def test_get(self):
        with self.given(
            'Getting the temperatures',
            '/apiv1/temperatures'
        ):
            assert status == 200
            assert 'cpu' in response.json
            assert 'gpu' in response.json

