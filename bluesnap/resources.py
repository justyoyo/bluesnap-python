from urlparse import urlparse
import re

from lxml import objectify, etree
from lxml.builder import ElementMaker
import requests
import xmltodict

from . import models
from .client import default as default_client


class Resource(object):
    class DoesNotExist(Exception):
        pass

    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""


class Shopper(Resource):
    path = '/services/2/shoppers'
    new_shopper_path = path + '/{shopper_id}'
    shopper_id_path_pattern = re.compile('{}/(\d+)'.format(path))  # /services/2/shoppers/(\d+)

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
                contact_info.to_xml('shopper'),
                getattr(E, 'payment-info')(
                    getattr(E, 'credit-cards-info')(
                        getattr(E, 'credit-card-info')(
                            contact_info.to_xml('billing'),
                            credit_card.to_xml()
                        )
                    )
                )
            ),
            models.WebInfo().to_xml()
        )

        xml = etree.tostring(shopper_element, pretty_print=True)

        print xml

        response = self.client.request('POST', self.path, data=xml)

        if response.status_code == requests.codes.created:
            new_shopper_url = urlparse(response.headers['location'])

            shopper_id = self.shopper_id_path_pattern.match(new_shopper_url.path).group(1)

            return self.find_by_shopper_id(int(shopper_id))

    def find_by_shopper_id(self, shopper_id):
        """
        :raise self.DoesNotExist
        :param shopper_id: BlueSnap shopper id
        :return: shopper dictionary
        """
        response = self.client.request('GET', self.new_shopper_path.format(shopper_id=shopper_id))

        if response.status_code == requests.codes.ok:
            return xmltodict.parse(response.content).get(u'shopper')
        else:
            raise self.DoesNotExist('Shopper with id {} does not exist')

    def find_by_seller_shopper_id(self, seller_shopper_id):
        """
        :raise self.DoesNotExist
        :param seller_shopper_id: Seller-specific shopper id
        :return: shopper dictionary
        """
        return self.find_by_shopper_id('{seller_shopper_id},{seller_id}'.format(
            seller_shopper_id=seller_shopper_id,
            seller_id=self.client.seller_id))


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
