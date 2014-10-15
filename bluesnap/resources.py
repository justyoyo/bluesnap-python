from urlparse import urlparse
import re

from lxml import objectify, etree
from lxml.builder import ElementMaker
import requests
import xmltodict

from . import models
from .client import default as default_client
from .exceptions import APIError


class Resource(object):
    class DoesNotExist(Exception):
        pass

    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""

    def request(self, method, path, data=None):
        response, body = self.client.request(method, path, data)
        return response, body


class Shopper(Resource):
    shoppers_path = '/services/2/shoppers'
    shopper_path = shoppers_path + '/{shopper_id}'
    shopper_id_path_pattern = re.compile('{}/(\d+)'.format(shoppers_path))  # /services/2/shoppers/(\d+)

    def find_by_shopper_id(self, shopper_id):
        """
        :raise self.DoesNotExist
        :param shopper_id: BlueSnap shopper id
        :return: shopper dictionary
        """

        try:
            response, body = self.request('GET', self.shopper_path.format(shopper_id=shopper_id))
        except APIError:
            raise self.DoesNotExist('Shopper with shopper_id "{}" does not exist', shopper_id)

        return body['shopper']

    def find_by_seller_shopper_id(self, seller_shopper_id):
        """
        :raise self.DoesNotExist
        :param seller_shopper_id: Seller-specific shopper id
        :return: shopper dictionary
        """
        return self.find_by_shopper_id('{seller_shopper_id},{seller_id}'.format(
            seller_shopper_id=seller_shopper_id,
            seller_id=self.client.seller_id))

    def _create_shopper_element(self, contact_info, credit_card=None, seller_shopper_id=None):
        # noinspection PyPep8Naming
        E = self.client.E

        credit_cards_info = []
        if credit_card is not None:
            credit_cards_info.append(getattr(E, 'credit-card-info')(
                contact_info.to_xml('billing'),
                credit_card.to_xml()
            ))

        shopper_info = []
        if seller_shopper_id is not None:
            shopper_info.append(getattr(E, 'seller-shopper-id')(seller_shopper_id))

        return E.shopper(
            getattr(E, 'shopper-info')(
                getattr(E, 'store-id')(self.client.store_id),
                getattr(E, 'shopper-currency')(self.client.currency),
                E.locale(self.client.locale),
                contact_info.to_xml('shopper'),
                getattr(E, 'payment-info')(
                    getattr(E, 'credit-cards-info')(*credit_cards_info)
                ),
                *shopper_info
            ),
            models.WebInfo().to_xml()
        )

    def create(self, contact_info, credit_card=None, seller_shopper_id=None, return_id=True):
        """
        Creates a new shopper
        :type contact_info: models.ContactInfo
        :type credit_card: models.AbstractCreditCard
        :param seller_shopper_id: Seller-specific shopper id
        :param return_id: If True, returns the BlueSnap shopper id. If False, fetches and returns the shopper object
        :return: Depends on return_id. See param description above
        """
        shopper_element = self._create_shopper_element(contact_info, credit_card, seller_shopper_id)
        data = etree.tostring(shopper_element)

        response, body = self.request('POST', self.shoppers_path, data=data)

        # Extract shopper id from location header
        new_shopper_url = urlparse(response.headers['location'])
        shopper_id = self.shopper_id_path_pattern.match(new_shopper_url.path).group(1)

        if return_id:
            return shopper_id
        else:
            return self.find_by_shopper_id(shopper_id)

    def update(self, shopper_id, contact_info, credit_card=None):
        """
        Updates an existing shopper
        :param shopper_id: BlueSnap shopper id
        :type contact_info: models.ContactInfo
        :type credit_card: models.AbstractCreditCard
        :rtype: bool
        """
        shopper_element = self._create_shopper_element(contact_info, credit_card)
        data = etree.tostring(shopper_element)

        try:
            response, _ = self.request('PUT', self.shopper_path.format(shopper_id=shopper_id), data=data)
        except APIError:
            raise self.DoesNotExist('Shopper with shopper_id "{}" does not exist', shopper_id)

        return response.status_code == requests.codes.no_content


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

        response, body = self.request('POST', self.path, data=etree.tostring(order_element))
        return body['order']
