from bluesnap.exceptions import APIError
from unittest import TestCase

from mock import MagicMock

from bluesnap.models import ContactInfo, PlainCreditCard
from bluesnap.resources import Order, Shopper
import helper


class ShopperTestCase(TestCase):
    def setUp(self):
        helper.configure_client()

        self.contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gb',
            phone='07777777777')

        self.credit_card = PlainCreditCard(**helper.DUMMY_CARD_VISA)
        self.second_credit_card = PlainCreditCard(**helper.DUMMY_CARD_MASTERCARD)
        self.third_credit_card = PlainCreditCard(**helper.DUMMY_CARD_AMEX)

    def test_create_with_valid_contact_info_returning_id(self):
        shopper = Shopper()
        shopper_id = shopper.create(
            contact_info=self.contact_info)

        self.assertIsNotNone(shopper_id)

    def test_create_with_valid_contact_info_returning_object(self):
        shopper = Shopper()

        shopper_id = shopper.create(
            contact_info=self.contact_info)
        shopper_obj = shopper.find_by_shopper_id(shopper_id)

        self.assertIsInstance(shopper_obj, dict)
        shopper_info = shopper_obj['shopper-info']
        shopper_contact_info = shopper_info['shopper-contact-info']
        self.assertEqual(shopper_contact_info['first-name'], self.contact_info.first_name)
        self.assertEqual(shopper_contact_info['last-name'], self.contact_info.last_name)
        self.assertEqual(shopper_info['store-id'], shopper.client.default_store_id)
        self.assertIsNone(shopper_info['payment-info']['credit-cards-info'])

    def test_create_with_valid_contact_info_and_credit_card(self):
        shopper = Shopper()

        shopper_id = shopper.create(
            contact_info=self.contact_info,
            credit_card=self.credit_card)
        shopper_obj = shopper.find_by_shopper_id(shopper_id)

        self.assertIsInstance(shopper_obj, dict)
        shopper_info = shopper_obj['shopper-info']
        shopper_contact_info = shopper_info['shopper-contact-info']
        self.assertEqual(shopper_contact_info['first-name'], self.contact_info.first_name)
        self.assertEqual(shopper_contact_info['last-name'], self.contact_info.last_name)
        self.assertEqual(shopper_info['store-id'], shopper.client.default_store_id)

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
        with self.assertRaisesRegexp(APIError, 'User: API_\d+ is not authorized to view shopper: 0'):
            Shopper().find_by_shopper_id('0')

        with self.assertRaisesRegexp(
                APIError,
                'User: API_\d+ is not authorized to view seller shopper: bogus_seller_shopper_id'):
            Shopper().find_by_seller_shopper_id('bogus_seller_shopper_id')

    def test_update_fails_with_invalid_shopper_id(self):
        shopper = Shopper()

        with self.assertRaisesRegexp(APIError, 'User: API_\d+ is not authorized to update shopper: 0'):
            shopper.update(
                '0',
                contact_info=self.contact_info)

    def test_add_shopper_credit_card(self):
        # Create a shopper, ensuring no credit card info was added
        shopper = Shopper()
        shopper_id = shopper.create(
            contact_info=self.contact_info)
        shopper_obj = shopper.find_by_shopper_id(shopper_id)
        self.assertIsNone(shopper_obj['shopper-info']['payment-info']['credit-cards-info'])

        # Add first credit card
        update_successful = shopper.update(
            shopper_id=shopper_id,
            contact_info=self.contact_info,
            credit_card=self.credit_card)
        self.assertTrue(update_successful)

        shopper_obj = shopper.find_by_shopper_id(shopper_id)
        credit_card_info = shopper_obj['shopper-info']['payment-info']['credit-cards-info']['credit-card-info']
        self.assertIsInstance(credit_card_info['credit-card'], dict)
        self.assertEqual(credit_card_info['credit-card']['card-last-four-digits'], self.credit_card.card_number[-4:])
        self.assertEqual(credit_card_info['credit-card']['card-type'], self.credit_card.card_type)

        # Add second credit card
        update_successful = shopper.update(
            shopper_id=shopper_id,
            contact_info=self.contact_info,
            credit_card=self.second_credit_card)
        self.assertTrue(update_successful)

        shopper_obj = shopper.find_by_shopper_id(shopper_id)
        credit_cards_info = shopper_obj['shopper-info']['payment-info']['credit-cards-info']['credit-card-info']
        self.assertIsInstance(credit_cards_info, list)
        self.assertEqual(len(credit_cards_info), 2)

        # Last added credit card displays first???
        self.assertEqual(credit_cards_info[0]['credit-card']['card-last-four-digits'],
                         self.second_credit_card.card_number[-4:])
        self.assertEqual(credit_cards_info[0]['credit-card']['card-type'],
                         self.second_credit_card.card_type)
        self.assertEqual(credit_cards_info[1]['credit-card']['card-last-four-digits'],
                         self.credit_card.card_number[-4:])
        self.assertEqual(credit_cards_info[1]['credit-card']['card-type'],
                         self.credit_card.card_type)

        # Add third credit card
        update_successful = shopper.update(
            shopper_id=shopper_id,
            contact_info=self.contact_info,
            credit_card=self.third_credit_card)
        self.assertTrue(update_successful)

        shopper_obj = shopper.find_by_shopper_id(shopper_id)
        credit_cards_info = shopper_obj['shopper-info']['payment-info']['credit-cards-info']['credit-card-info']
        self.assertIsInstance(credit_cards_info, list)
        self.assertEqual(len(credit_cards_info), 3)

        # Last added credit card displays first
        self.assertEqual(credit_cards_info[0]['credit-card']['card-last-four-digits'],
                         self.third_credit_card.card_number[-4:])
        self.assertEqual(credit_cards_info[0]['credit-card']['card-type'],
                         self.third_credit_card.card_type)
        self.assertEqual(credit_cards_info[1]['credit-card']['card-last-four-digits'],
                         self.second_credit_card.card_number[-4:])
        self.assertEqual(credit_cards_info[1]['credit-card']['card-type'],
                         self.second_credit_card.card_type)
        self.assertEqual(credit_cards_info[2]['credit-card']['card-last-four-digits'],
                         self.credit_card.card_number[-4:])
        self.assertEqual(credit_cards_info[2]['credit-card']['card-type'],
                         self.credit_card.card_type)


class OrderTestCase(TestCase):
    def setUp(self):
        helper.configure_client()

        self.contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gb',
            phone='07777777777')

        self.credit_card = PlainCreditCard(**helper.DUMMY_CARD_VISA)

        shopper = Shopper()

        self.shopper_id = shopper.create(
            contact_info=self.contact_info,
            credit_card=self.credit_card)

        self.shopper_id_without_credit_card = shopper.create(
            contact_info=self.contact_info)

    def test_shopper_with_credit_card_creating_order_succeeds(self):
        order = Order()
        # order.create(
        #     shopper_id=self.shopper_id,
        #     sku_id=helper.TEST_PRODUCT_SKU_ID,
        #     amount_in_pence=100
        # )
