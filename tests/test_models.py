import unittest

from lxml import etree

from bluesnap import models
from helper import DUMMY_CARD_VISA, get_xml_schema



class PlainCreditCardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = DUMMY_CARD_VISA

        self.model = models.PlainCreditCard

        self.instance = self.model(
            card_type=self.card['card_type'],
            expiration_month=self.card['expiration_month'],
            expiration_year=self.card['expiration_year'],
            card_number=self.card['card_number'],
            security_code=self.card['security_code']
        )

    def test_to_xml_returns_correct_format(self):
        xml = self.instance.to_xml()
        get_xml_schema('credit-card-info.xsd').assertValid(xml)
