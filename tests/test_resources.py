import unittest

from mock import MagicMock

from bluesnap.models import ContactInfo, PlainCreditCard
from bluesnap.resources import Order, Shopper
from helper import configure_client, DUMMY_CARD_VISA


configure_client()


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        self.contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gbe',
            phone='07777777777')

        self.credit_card = PlainCreditCard(
            card_type=DUMMY_CARD_VISA['card_type'],
            expiration_month=DUMMY_CARD_VISA['expiration_month'],
            expiration_year=DUMMY_CARD_VISA['expiration_year'],
            card_number=DUMMY_CARD_VISA['card_number'],
            security_code=DUMMY_CARD_VISA['security_code'])

    def test_shopper_xml(self):
        shopper = Shopper()
        shopper.create(
            contact_info=self.contact_info,
            credit_card=self.credit_card)
        self.assertTrue(False)  # TODO

    def test_find_by_with_valid_shopper_id(self):
        pass  # TODO

    def test_find_by_seller_shopper_id(self):
        seller_id = 'seller_id'
        seller_shopper_id = 'seller_shopper_id'

        # Set up
        shopper = Shopper()
        shopper.client.seller_id = seller_id
        shopper.find_by_shopper_id = MagicMock()

        shopper.find_by_seller_shopper_id(seller_shopper_id)
        shopper.find_by_shopper_id.assert_called_once_with('{seller_shopper_id},{seller_id}'.format(
            seller_shopper_id=seller_shopper_id,
            seller_id=seller_id))
