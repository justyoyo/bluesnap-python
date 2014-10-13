from collections import namedtuple
import platform

import requests

from .client import default as default_client
from .version import __version__


class Model(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""

    def to_xml(self):
        raise NotImplementedError('{}.to_xml(self) is not implemented'.format(self.__class__.__name__))


class AbstractCreditCard(Model):
    def __init__(self, card_type, expiration_month, expiration_year, client=None):
        super(AbstractCreditCard, self).__init__(
            client=client)

        self.card_type = card_type
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year


class PlainCreditCard(AbstractCreditCard):
    def __init__(self, card_type, expiration_month, expiration_year, card_number, security_code, client=None):
        super(PlainCreditCard, self).__init__(
            card_type=card_type,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            client=client)

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


class EncryptedCreditCard(AbstractCreditCard):
    def __init__(self, card_type, expiration_month, expiration_year, encrypted_card_number, encrypted_security_code,
                 client=None):
        super(EncryptedCreditCard, self).__init__(
            card_type=card_type,
            expiration_month=expiration_month,
            expiration_year=expiration_year,
            client=client)

        self.encrypted_card_number = encrypted_card_number
        self.encrypted_security_code = encrypted_security_code

    def to_xml(self):
        """
        Converts EncryptedCreditCard object to XML object:

        <credit-card>
            <encrypted-card-number>...</card-number>
            <card-type>VISA</card-type>
            <expiration-month>10</expiration-month>
            <expiration-year>2014</expiration-year>
            <encrypted-security-code>....</security-code>
        </credit-card>

        :return: lxml.etree._Element
        """
        E = self.client.E

        return getattr(E, 'credit-card')(
            getattr(E, 'encrypted-card-number')(self.encrypted_card_number),
            getattr(E, 'card-type')(self.card_type),
            getattr(E, 'expiration-month')(str(self.expiration_month)),
            getattr(E, 'expiration-year')(str(self.expiration_year)),
            getattr(E, 'encrypted-security-code')(self.encrypted_security_code)
        )


class WebInfo(Model):
    def __init__(self, ip=None, user_agent=None, client=None):
        super(WebInfo, self).__init__(
            client=client
        )

        # Set dummy IP for now
        self.ip = ip or '0.0.0.0'
        self.user_agent = user_agent or self.default_user_agent

    @property
    def default_user_agent(self):
        """
        Generate default user agent based on library repo name, Python version and requests version
        :return: string
        """
        library_versions = 'requests {}; python {}'.format(requests.__version__, platform.version())
        return 'justyoyo/bluesnap-python {} ({})'.format(__version__, library_versions)

    def to_xml(self):
        """
        Converts WebInfo object to XML object:

        <web-info>
            <ip>0.0.0.0</ip>
            <user-agent></user-agent>
        </web-info>

        :return: lxml.etree._Element
        """
        E = self.client.E

        return getattr(E, 'web-info')(
            E.ip(self.ip),
            getattr(E, 'user-agent')(self.user_agent)
        )

ContactInfo = namedtuple('ContactInfo',
                         ['first_name', 'last_name', 'email', 'address_1', 'city', 'zip', 'country', 'phone'])
