import datetime
import os

from lxml import etree


now = datetime.datetime.now()
future = now + datetime.timedelta(days=1)

__path__ = os.path.dirname(os.path.realpath(__file__))

NAMESPACE_PREFIX = '{http://ws.plimus.com}'

SANDBOX_CLIENT_CONFIG = {
    'env': 'sandbox',
    'username': 'API_14127729102161320867365',
    'password': 'JustYoyo1',
    'default_store_id': '13945',
    'seller_id': '397608',
    'default_currency': 'GBP'
}

TEST_PRODUCT_SKU_ID = '2152476'

# Dummy cards taken from
# http://home.bluesnap.com/integrationguide/default.htm#WordManual/Working_with_Sandbox_Testing.htm
# http://avners.info/api/constant-values/test-credit-card-numbers

DUMMY_CARD_VISA = {
    'card_type': 'VISA',
    'card_number': '4111111111111111',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '123',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_VISA__EXPIRED = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 4,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_VISA__INSUFFICIENT_FUNDS = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 5,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_VISA__INVALID_CARD_NUMBER = {
    'card_type': 'VISA',
    'card_number': '4917484589897107',
    'expiration_month': 8,
    'expiration_year': 2018,
    'security_code': '411',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_MASTERCARD = {
    'card_type': 'MASTERCARD',
    'card_number': '5105105105105100',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '123',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_AMEX = {
    'card_type': 'AMEX',
    'card_number': '378282246310005',
    'expiration_month': future.month,
    'expiration_year': future.year,
    'security_code': '4111',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARD_AMEX__AUTH_FAIL = {
    'card_type': 'AMEX',
    'card_number': '378282246310005',
    'expiration_month': 5,
    'expiration_year': 2018,
    'security_code': '4111',
    'encrypted_card_number': r'ENCRYPTED CARD NUMBER',
    'encrypted_security_code': r'ENCRYPTED SECURITY CODE'
}

DUMMY_CARDS = (
    ('Visa', DUMMY_CARD_VISA),
    ('MasterCard', DUMMY_CARD_MASTERCARD),
    ('American Express', DUMMY_CARD_AMEX)
)


def configure_client():
    from bluesnap import client
    client.configure(**SANDBOX_CLIENT_CONFIG)


def get_xml_schema(file_name):
    return etree.XMLSchema(etree.parse(os.path.join(__path__, 'schemas', file_name)))
