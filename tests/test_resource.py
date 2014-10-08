import unittest

from bluesnap.resource import Shopper


class ShopperTestCase(unittest.TestCase):
    def test_shopper_xml(self):
        shopper = Shopper().create()
        # self.assertTrue(False)
