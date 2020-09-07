from bddrest import status, response

from .helpers import LocalApplicationTestCase


class TestOpenConnect(LocalApplicationTestCase):

    def test_status(self):
        with self.given(
            'Status of open vpn',
            '/apiv1/openconnects',
            'STATUS',
        ):
            assert status == 200
            assert 'status' in response.json

    def test_reset(self):
        with self.given(
            'Reseting the open vpn',
            '/apiv1/openconnects',
            'RESET',
        ):
            assert status == 200
            assert 'status' in response.json

    def test_stop(self):
        with self.given(
            'Stop the open vpn',
            '/apiv1/openconnects',
            'STOP',
        ):
            assert status == 200
            assert 'status' in response.json

