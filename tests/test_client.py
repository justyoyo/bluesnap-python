import unittest

from bluesnap.client import Client


class ClientTestCase(unittest.TestCase):
    dummy_credentials = {
        'username': 'username',
        'password': 'password',
        'default_store_id': '100',
    }

    def setUp(self):
        self.client = Client(env='live', **self.dummy_credentials)

    def test_env(self):
        self.assertEqual(Client.ENDPOINTS.keys(), ['live', 'sandbox'])

        for env, endpoint_url in Client.ENDPOINTS.iteritems():
            client = Client(env=env, **self.dummy_credentials)
            self.assertEqual(client.endpoint_url, endpoint_url)
