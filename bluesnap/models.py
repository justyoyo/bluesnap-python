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
    def __init__(self, ip=None, remote_host=None, user_agent=None, client=None):
        super(WebInfo, self).__init__(
            client=client
        )

        self.ip = ip or '0.0.0.0'
        self.remote_host = remote_host or 'localhost'
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
            <remote-host>localhost</remote-host>
            <user-agent></user-agent>
        </web-info>

        :return: lxml.etree._Element
        """
        E = self.client.E

        return getattr(E, 'web-info')(
            E.ip(self.ip),
            getattr(E, 'remote-host')(self.remote_host),
            getattr(E, 'user-agent')(self.user_agent)
        )


class ContactInfo(Model):
    ELEMENT_NAME = None
    NONE_PLACEHOLDER = '(Empty)'

    def __init__(self, email,
                 first_name=None, last_name=None, address_1=None, city=None,
                 zip=None, country=None, phone=None, client=None):
        super(ContactInfo, self).__init__(
            client=client
        )

        self.email = email
        self.first_name = first_name or self.NONE_PLACEHOLDER
        self.last_name = last_name or self.NONE_PLACEHOLDER
        self.address_1 = address_1 or self.NONE_PLACEHOLDER
        self.city = city or self.NONE_PLACEHOLDER
        self.zip = zip or self.NONE_PLACEHOLDER
        self.country = country or self.NONE_PLACEHOLDER
        self.phone = phone or self.NONE_PLACEHOLDER

    @property
    def xml_element_name(self):
        if self.ELEMENT_NAME:
            return '{}-contact-info'.format(self.ELEMENT_NAME)
        else:
            return 'contact-info'

    def to_xml(self):
        """
        Converts WebInfo object to XML object:

        <{xml_element_name}-contact-info>
            <first-name>John</first-name>
            <last-name>Doe</last-name>
            <email>dev@justyoyo.com</email>
            <address1>Address 1</address1>
            <city>City</city>
            <zip>SW5</zip>
            <country>gb</country>
            <phone>07777777777</phone>
        </{xml_element_name}-contact-info>

        :return: lxml.etree._Element
        """
        E = self.client.E

        return getattr(E, self.xml_element_name)(
            getattr(E, 'first-name')(self.first_name),
            getattr(E, 'last-name')(self.last_name),
            E.email(self.email),
            E.address1(self.address_1),
            E.city(self.city),
            E.zip(self.zip),
            E.country(self.country),
            E.phone(self.phone)
        )
