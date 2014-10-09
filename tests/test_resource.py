import unittest

from bluesnap.client import configure as configure_client
from bluesnap.resource import Shopper

from helper import SANDBOX_CLIENT_CONFIG


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        configure_client(**SANDBOX_CLIENT_CONFIG)

    def test_shopper_xml(self):
        shopper = Shopper().create()
        # self.assertTrue(False)
