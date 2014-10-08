import unittest

from bluesnap.client import Client


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(env='live')

    def test_env(self):
        self.assertEqual(Client.ENDPOINTS.keys(), ['live', 'sandbox'])

        for env, endpoint_url in Client.ENDPOINTS.iteritems():
            client = Client(env=env)
            self.assertEqual(client.endpoint_url, endpoint_url)
