import unittest

from bluesnap.client import configure as configure_client
from bluesnap.models import ContactInfo, PlaintextCreditCard
from bluesnap.resources import Order, Shopper

from helper import SANDBOX_CLIENT_CONFIG


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        configure_client(**SANDBOX_CLIENT_CONFIG)

    def test_shopper_xml(self):
        contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            address_1='(Empty)',
            city='(Empty)',
            zip='(Empty)',
            country='gb',
            phone='07777777777'
        )

        credit_card = PlaintextCreditCard(
            card_type='VISA',
            expiration_month='12',
            expiration_year='2015',
            card_number='4111111111111111',
            security_code='111'
        )

        shopper = Shopper()
        shopper.create(
            contact_info=contact_info,
            credit_card=credit_card)
        # self.assertTrue(False)

    def test_order_xml(self):
        order = Order().create()
