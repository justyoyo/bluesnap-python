from urlparse import urlparse

from lxml import objectify, etree
from lxml.builder import ElementMaker
import requests

from . import models
from .client import default as default_client


class Resource(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""


class Shopper(Resource):
    path = '/services/2/shoppers'

    def create(self, contact_info, credit_card):
        """
        :type contact_info : models.ContactInfo
        :type credit_card : models.AbstractCreditCard
        """
        # noinspection PyPep8Naming
        E = self.client.E

        # noinspection PyCallByClass
        shopper_element = E.shopper(
            getattr(E, 'shopper-info')(
                getattr(E, 'store-id')(self.client.default_store_id),
                getattr(E, 'shopper-currency')('GBP'),
                E.locale('en'),
                # getattr(E, 'seller-shopper-id')('1234'),
                models.ShopperContactInfo.to_xml(contact_info),
                getattr(E, 'payment-info')(
                    getattr(E, 'credit-cards-info')(
                        getattr(E, 'credit-card-info')(
                            models.BillingContactInfo.to_xml(contact_info),
                            credit_card.to_xml()
                        )
                    )
                )
            ),
            models.WebInfo().to_xml()
        )

        xml = etree.tostring(shopper_element, pretty_print=True)
        print xml

        r = self.client.request('POST', self.path, data=xml)

        if r.status_code == requests.codes.created:
            new_shopper_url = urlparse(r.headers['location'])

            print new_shopper_url

            r = self.client.request('GET', new_shopper_url.path)
            shopper_element = etree.XML(r.content)
            print etree.tostring(shopper_element, pretty_print=True)
        else:
            messages = etree.XML(r.content)

            for message in messages:
                print 'ok'
                print etree.tostring(message, pretty_print=True)
                # data = {}
                # for attr in message.iter():
                #     data[attr.tag] = attr.text

                # print data
                # print message.findtext('{*}code')
                # print message.findtext('{*}description')
                # if hasattr(message, 'description'):
                #     print message.description

            # print dir(messages), messages.__class__

            # for message in messages.message:
            #     print message

            # print etree.tostring(messages, pretty_print=True)

            #
            # print messages_schema.CreateFromDocument(r.text)

        # raise Exception


class Order(Resource):
    path = '/services/2/orders'

    def create(self):
        E = ElementMaker(namespace=self.client.NAMESPACE,
                         nsmap={None: self.client.NAMESPACE})

        ORDER = E.order
        ORDERING_SHOPPER = getattr(E, 'ordering-shopper')
        SHOPPER_ID = getattr(E, 'shopper-id')

        CART = E.cart
        CART_ITEM = getattr(E, 'cart-item')
        SKU = E.sku
        SKU_ID = getattr(E, 'sku-id')
        SKU_CHARGE_PRICE = getattr(E, 'sku-charge-price')
        CHARGE_TYPE = getattr(E, 'charge-type')
        AMOUNT = E.amount
        CURRENCY = E.currency
        QUANTITY = E.quantity
        EXPECTED_TOTAL_PRICE = getattr(E, 'expected-total-price')

        order_element = ORDER(
            ORDERING_SHOPPER(
                SHOPPER_ID('19572924'),
                models.WebInfo().to_xml()
            ),
            CART(
                CART_ITEM(
                    SKU(
                        SKU_ID('2152476'),
                        SKU_CHARGE_PRICE(
                            CHARGE_TYPE('initial'),
                            AMOUNT('1.00'),
                            CURRENCY('GBP')
                        )
                    ),
                    QUANTITY('1'),
                ),
            ),
            EXPECTED_TOTAL_PRICE(
                AMOUNT('1.00'),
                CURRENCY('GBP')
            )
        )

        xml = etree.tostring(order_element, pretty_print=True)
        print xml

        r = self.client.request('POST', self.path, data=xml)

        if r.status_code == requests.codes.created:
            order_element = etree.XML(r.content)
            print etree.tostring(order_element, pretty_print=True)
        else:
            print r.body
            messages = etree.XML(r.content)
            print etree.tostring(messages, pretty_print=True)
