import unittest

from bluesnap.client import BluesnapClient


class BluesnapClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = BluesnapClient(env='live')

    def test_env(self):
        self.assertEqual(BluesnapClient.ENDPOINTS.keys(), ['live', 'sandbox'])

        for env, endpoint_url in BluesnapClient.ENDPOINTS.iteritems():
            client = BluesnapClient(env=env)
            self.assertEqual(client.endpoint_url, endpoint_url)
