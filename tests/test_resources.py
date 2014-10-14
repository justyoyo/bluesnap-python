import unittest

from bluesnap.models import ContactInfo, PlainCreditCard
from bluesnap.resources import Order, Shopper

from helper import configure_client, DUMMY_CARD_VISA


configure_client()


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_shopper_xml(self):
        contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gb',
            phone='07777777777'
        )

        credit_card = PlainCreditCard(
            card_type=DUMMY_CARD_VISA['card_type'],
            expiration_month=DUMMY_CARD_VISA['expiration_month'],
            expiration_year=DUMMY_CARD_VISA['expiration_year'],
            card_number=DUMMY_CARD_VISA['card_number'],
            security_code=DUMMY_CARD_VISA['security_code']
        )

        shopper = Shopper()
        shopper.create(
            contact_info=contact_info,
            credit_card=credit_card)
        self.assertTrue(False)

    # def test_order_xml(self):
    #     order = Order().create()
