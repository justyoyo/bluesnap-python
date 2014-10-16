from bluesnap.exceptions import APIError
from unittest import TestCase

from mock import MagicMock

from bluesnap.models import ContactInfo, PlainCreditCard
from bluesnap.resources import Order, Shopper
import helper


class ShopperTestCase(TestCase):
    maxDiff = None

    def setUp(self):
        helper.configure_client()

        self.contact_info = ContactInfo(
            first_name='John',
            last_name='Doe',
            email='test@justyoyo.com',
            zip='SW5',
            country='gb',
            phone='07777777777')

        self.credit_card = PlainCreditCard(
            card_type=helper.DUMMY_CARD_VISA['card_type'],
            expiration_month=helper.DUMMY_CARD_VISA['expiration_month'],
            expiration_year=helper.DUMMY_CARD_VISA['expiration_year'],
            card_number=helper.DUMMY_CARD_VISA['card_number'],
            security_code=helper.DUMMY_CARD_VISA['security_code'])
        self.second_credit_card = PlainCreditCard(
            card_type=helper.DUMMY_CARD_MASTERCARD['card_type'],
            expiration_month=helper.DUMMY_CARD_MASTERCARD['expiration_month'],
            expiration_year=helper.DUMMY_CARD_MASTERCARD['expiration_year'],
            card_number=helper.DUMMY_CARD_MASTERCARD['card_number'],
            security_code=helper.DUMMY_CARD_MASTERCARD['security_code'])
        self.third_credit_card = PlainCreditCard(
            card_type=helper.DUMMY_CARD_AMEX['card_type'],
            expiration_month=helper.DUMMY_CARD_AMEX['expiration_month'],
            expiration_year=helper.DUMMY_CARD_AMEX['expiration_year'],
            card_number=helper.DUMMY_CARD_AMEX['card_number'],
            security_code=helper.DUMMY_CARD_AMEX['security_code'])

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

        # TODO raise a more informative exception instead of a generic one
        with self.assertRaisesRegexp(APIError, 'Seller \d+ encountered a problem creating a new shopper due to incorrect input.'):
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
        # TODO raise a more informative exception instead of a generic one
        with self.assertRaisesRegexp(APIError, 'User: API_\d+ is not authorized to view shopper: 0'):
            Shopper().find_by_shopper_id('0')

        # TODO raise a more informative exception instead of a generic one
        with self.assertRaisesRegexp(
                APIError,
                'User: API_\d+ is not authorized to view seller shopper: bogus_seller_shopper_id'):
            Shopper().find_by_seller_shopper_id('bogus_seller_shopper_id')

    def test_update_fails_with_invalid_shopper_id(self):
        shopper = Shopper()

        # TODO raise a more informative exception instead of a generic one
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

        # The order of the credit cards is not known, so we sort the items before comparing.
        cards = map(lambda c: dict(c['credit-card']), credit_cards_info)
        self.assertItemsEqual(
            cards,
            [{'card-last-four-digits': self.credit_card.card_number[-4:],
              'card-type': self.credit_card.card_type},
             {'card-last-four-digits': self.second_credit_card.card_number[-4:],
              'card-type': self.second_credit_card.card_type}])

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
        cards = map(lambda c: dict(c['credit-card']), credit_cards_info)
        self.assertItemsEqual(
            cards,
            [{'card-last-four-digits': self.credit_card.card_number[-4:],
              'card-type': self.credit_card.card_type},
             {'card-last-four-digits': self.second_credit_card.card_number[-4:],
              'card-type': self.second_credit_card.card_type},
             {'card-last-four-digits': self.third_credit_card.card_number[-4:],
              'card-type': self.third_credit_card.card_type}])


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
        amount_in_pence = 150
        amount = amount_in_pence / 100.0
        description = 'order description'
        order = Order()
        order_obj = order.create(
            shopper_id=self.shopper_id,
            sku_id=helper.TEST_PRODUCT_SKU_ID,
            amount_in_pence=amount_in_pence,
            description=description)

        self.assertIsInstance(order_obj, dict)
        self.assertEqual(order_obj['ordering-shopper']['shopper-id'], self.shopper_id)
        self.assertEqual(order_obj['cart']['charged-currency'], order.client.currency)
        self.assertEqual(order_obj['cart']['cart-item']['sku']['sku-id'], helper.TEST_PRODUCT_SKU_ID)
        self.assertEqual(int(order_obj['cart']['cart-item']['quantity']), 1)
        self.assertEqual(float(order_obj['cart']['cart-item']['item-sub-total']), amount)
        self.assertEqual(float(order_obj['cart']['tax']), 0.0)
        self.assertEqual(int(order_obj['cart']['tax-rate']), 0)
        self.assertEqual(float(order_obj['cart']['total-cart-cost']), amount)
        self.assertIsNotNone(order_obj['post-sale-info']['invoices']['invoice']['invoice-id'])
        self.assertIsNotNone(order_obj['post-sale-info']['invoices']['invoice']['url'])
        self.assertIsNotNone(
            order_obj['post-sale-info']['invoices']['invoice']['financial-transactions']['financial-transaction'][
                'soft-descriptor'], description)
        self.assertEqual(float(
            order_obj['post-sale-info']['invoices']['invoice']['financial-transactions']['financial-transaction'][
                'amount']), amount)
        self.assertEqual(
            order_obj['post-sale-info']['invoices']['invoice']['financial-transactions']['financial-transaction'][
                'currency'], order.client.currency)
        self.assertEqual(
            order_obj['post-sale-info']['invoices']['invoice']['financial-transactions']['financial-transaction'][
                'credit-card']['card-last-four-digits'], self.credit_card.card_number[-4:])

    def test_shopper_without_credit_card_creating_order_fails(self):
        order = Order()
        with self.assertRaises(APIError) as e:
            order.create(
                shopper_id=self.shopper_id_without_credit_card,
                sku_id=helper.TEST_PRODUCT_SKU_ID,
                amount_in_pence=100)

        # TODO raise a more informative exception instead of a generic one
        self.assertListEqual(
            e.messages,
            [{'code': '15009',
              'description': 'Order creation failure, since no payment information was provided.'}])
