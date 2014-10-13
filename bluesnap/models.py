from collections import namedtuple

from .client import default as default_client


class Model(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""


class PlainCreditCard(Model):
    def __init__(self, card_type, expiration_month, expiration_year, card_number, security_code, client=None):
        super(PlainCreditCard, self).__init__(client)

        self.card_type = card_type
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.card_number = card_number
        self.security_code = security_code

    def to_xml(self):
        """
        Converts PlainCreditCard object to XML object:

        <credit-card>
            <card-number>4111111111111111</card-number>
            <card-type>VISA</card-type>
            <expiration-month>10</expiration-month>
            <expiration-year>2014</expiration-year>
            <security-code>123</security-code>
        </credit-card>

        :return: lxml.etree._Element
        """
        E = self.client.E

        return getattr(E, 'credit-card')(
            getattr(E, 'card-number')(self.card_number),
            getattr(E, 'card-type')(self.card_type),
            getattr(E, 'expiration-month')(str(self.expiration_month)),
            getattr(E, 'expiration-year')(str(self.expiration_year)),
            getattr(E, 'security-code')(self.security_code)
        )


ContactInfo = namedtuple('ContactInfo',
                         ['first_name', 'last_name', 'email', 'address_1', 'city', 'zip', 'country', 'phone'])

EncryptedCreditCard = namedtuple('EncryptedCreditCard',
                                 ['card_type', 'expiration_month', 'expiration_year', 'encrypted_card_number',
                                  'encrypted_security_code'])
