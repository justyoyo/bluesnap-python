import unittest
from bluesnap.exceptions import APIError

from mock import MagicMock

from bluesnap.models import ContactInfo, PlainCreditCard
from bluesnap.resources import Order, Shopper
from helper import configure_client, DUMMY_CARD_VISA


class ShopperTestCase(unittest.TestCase):
    def setUp(self):
        configure_client()

        self.contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gb',
            phone='07777777777')

        self.credit_card = PlainCreditCard(
            card_type=DUMMY_CARD_VISA['card_type'],
            expiration_month=DUMMY_CARD_VISA['expiration_month'],
            expiration_year=DUMMY_CARD_VISA['expiration_year'],
            card_number=DUMMY_CARD_VISA['card_number'],
            security_code=DUMMY_CARD_VISA['security_code'])

    def create_shopper(self, shopper):
        return shopper.create(
            contact_info=self.contact_info,
            credit_card=self.credit_card)

    def test_create_with_valid_contact_info_returning_id(self):
        shopper = Shopper()

        shopper_id = shopper.create(
            contact_info=self.contact_info,
            return_id=True)

        self.assertIsNotNone(shopper_id)

    def test_create_with_valid_contact_info_returning_object(self):
        shopper = Shopper()
        mocked_shopper_obj = MagicMock()
        shopper.find_by_shopper_id = MagicMock(return_value=mocked_shopper_obj)

        shopper_obj = shopper.create(
            contact_info=self.contact_info,
            return_id=False)

        self.assertEqual(shopper.find_by_shopper_id.call_count, 1)
        self.assertEqual(shopper_obj, mocked_shopper_obj)

    def test_create_with_valid_contact_info_and_credit_card(self):
        shopper = Shopper()
        mocked_shopper_obj = MagicMock()
        shopper.find_by_shopper_id = MagicMock(return_value=mocked_shopper_obj)

        shopper_obj = shopper.create(
            contact_info=self.contact_info,
            credit_card=self.credit_card,
            return_id=False)
        self.assertEqual(shopper.find_by_shopper_id.call_count, 1)
        self.assertEqual(shopper_obj, mocked_shopper_obj)

    def test_create_with_invalid_parameters(self):
        shopper = Shopper()

        with self.assertRaises(APIError):
            shopper.create(
                contact_info=ContactInfo(email=''),
                credit_card=self.credit_card)

    def test_find_by_shopper_id(self):
        shopper = Shopper()
        shopper_id = shopper.create(
            contact_info=self.contact_info)

        self.assertIsNotNone(shopper_id)

        # find_by_shopper_id
        shopper_obj = shopper.find_by_shopper_id(shopper_id)

        self.assertIsInstance(shopper_obj, dict)
        shopper_contact_info = shopper_obj['shopper-info']['shopper-contact-info']
        self.assertEqual(shopper_contact_info['first-name'], self.contact_info.first_name)
        self.assertEqual(shopper_contact_info['last-name'], self.contact_info.last_name)
        self.assertEqual(shopper_obj['shopper-info']['store-id'], shopper.client.default_store_id)

    def test_find_by_seller_shopper_id(self):
        seller_id = 'seller_id'
        seller_shopper_id = 'seller_shopper_id'

        # Set up
        shopper = Shopper()
        shopper.client.seller_id = seller_id
        shopper.find_by_shopper_id = MagicMock()

        # find_by_seller_shopper_id
        shopper.find_by_seller_shopper_id(seller_shopper_id)

        shopper.find_by_shopper_id.assert_called_once_with('{seller_shopper_id},{seller_id}'.format(
            seller_shopper_id=seller_shopper_id,
            seller_id=seller_id))

    def test_find_by_bogus_shopper_id_and_seller_shopper_id_raises_exception(self):
        with self.assertRaises(Shopper.DoesNotExist):
            Shopper().find_by_shopper_id('bogus_shopper_id')

        with self.assertRaises(Shopper.DoesNotExist):
            Shopper().find_by_seller_shopper_id('bogus_seller_shopper_id')

    def test_update_fails_with_invalid_shopper_id(self):
        shopper = Shopper()

        with self.assertRaises(Shopper.DoesNotExist):
            shopper.update(
                'bogus_shopper_id',
                contact_info=self.contact_info)
