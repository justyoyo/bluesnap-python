import unittest

from bluesnap.client import configure as configure_client
from bluesnap.resource import Shopper


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        configure_client(
            env='sandbox',
            username='API_14127729102161320867365',
            password='JustYoyo1',
            default_store_id='13945'
        )

    def test_shopper_xml(self):
        shopper = Shopper().create()
        # self.assertTrue(False)
