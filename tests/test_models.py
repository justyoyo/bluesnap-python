from unittest import TestCase

from bluesnap import models
from helper import NAMESPACE_PREFIX, DUMMY_CARD_VISA, get_xml_schema


class PlainCreditCardTestCase(TestCase):
    model = models.PlainCreditCard

    def setUp(self):
        self.card = DUMMY_CARD_VISA

        self.instance = self.model(
            card_type=self.card['card_type'],
            expiration_month=self.card['expiration_month'],
            expiration_year=self.card['expiration_year'],
            card_number=self.card['card_number'],
            security_code=self.card['security_code']
        )

        self.xml = self.instance.to_xml()

    def test_to_xml_returns_correct_schema(self):
        # Validate XML schema
        get_xml_schema('credit-card-info.xsd').assertValid(self.xml)

    def test_to_xml_sets_correct_values(self):
        # Validate values being set correctly
        for xml_key, dict_key in [('card-type', 'card_type'),
                                  ('expiration-month', 'expiration_month'),
                                  ('expiration-year', 'expiration_year'),
                                  ('card-number', 'card_number'),
                                  ('security-code', 'security_code')]:
            self.assertEqual(self.xml.find(NAMESPACE_PREFIX + xml_key).text, str(self.card[dict_key]))


class EncryptedCreditCardTestCase(TestCase):
    model = models.EncryptedCreditCard

    def setUp(self):
        self.card = DUMMY_CARD_VISA

        self.instance = self.model(
            card_type=self.card['card_type'],
            expiration_month=self.card['expiration_month'],
            expiration_year=self.card['expiration_year'],
            encrypted_card_number=self.card['encrypted_card_number'],
            encrypted_security_code=self.card['encrypted_security_code']
        )

        self.xml = self.instance.to_xml()

    # Test disabled because XML Schema given is incorrect as it does not correspond with that in the API docs.
    #
    # def test_to_xml_returns_correct_schema(self):
    #     # Validate XML schema
    #     get_xml_schema('credit-card-info.xsd').assertValid(self.xml)

    def test_to_xml_sets_correct_values(self):
        # Validate values being set correctly
        for xml_key, dict_key in [('card-type', 'card_type'),
                                  ('expiration-month', 'expiration_month'),
                                  ('expiration-year', 'expiration_year'),
                                  ('encrypted-card-number', 'encrypted_card_number'),
                                  ('encrypted-security-code', 'encrypted_security_code')]:
            element = self.xml.find(NAMESPACE_PREFIX + xml_key)

            self.assertIsNotNone(element, 'Cannot find element <{}/>'.format(NAMESPACE_PREFIX + xml_key))
            self.assertEqual(element.text, str(self.card[dict_key]))


class WebInfoTestCase(TestCase):
    model = models.WebInfo

    def setUp(self):
        self.instance = self.model()
        self.xml = self.instance.to_xml()

    def test_to_xml_returns_correct_schema(self):
    # Validate XML schema
        get_xml_schema('web-info.xsd').assertValid(self.xml)

    def test_to_xml_sets_correct_values(self):
        # Validate values being set correctly
        for xml_key, dict_key in [('ip', 'ip'),
                                  ('user-agent', 'user_agent')]:
            element = self.xml.find(NAMESPACE_PREFIX + xml_key)

            self.assertIsNotNone(element, 'Cannot find element <{}/>'.format(NAMESPACE_PREFIX + xml_key))
            self.assertEqual(element.text, getattr(self.instance, dict_key))
