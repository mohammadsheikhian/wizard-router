from bddrest import status, response

from .helpers import LocalApplicationTestCase


class TestOpenVPN(LocalApplicationTestCase):

    def test_status(self):
        with self.given(
            'Status of open vpn',
            '/apiv1/openvpns',
            'STATUS',
        ):
            assert status == 200
            assert 'status' in response.json

    def test_reset(self):
        with self.given(
            'Reseting the open vpn',
            '/apiv1/openvpns',
            'RESTART',
        ):
            assert status == 200
            assert 'status' in response.json

    def test_stop(self):
        with self.given(
            'Stop the open vpn',
            '/apiv1/openvpns',
            'STOP',
        ):
            assert status == 200
            assert 'status' in response.json

