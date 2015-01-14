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
        :param shopper_id: BlueSnap shopper id
        :return: shopper dictionary
        """
        response, body = self.request('GET', self.shopper_path.format(shopper_id=shopper_id))
        return body['shopper']

    def find_by_seller_shopper_id(self, seller_shopper_id):
        """
        :param seller_shopper_id: Seller-specific shopper id
        :return: shopper dictionary
        """
        return self.find_by_shopper_id('{seller_shopper_id},{seller_id}'.format(
            seller_shopper_id=seller_shopper_id,
            seller_id=self.client.seller_id))

    def _create_shopper_element(self, contact_info, credit_card=None,
                                seller_shopper_id=None, client_ip=None):
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
            models.WebInfo(ip=client_ip).to_xml()
        )

    def create(self, contact_info, credit_card=None, seller_shopper_id=None,
               client_ip=None):
        """
        Creates a new shopper
        :type contact_info: models.ContactInfo
        :type credit_card: models.AbstractCreditCard
        :param seller_shopper_id: Seller-specific shopper id
        :return: Returns the newly created BlueSnap shopper id
        """
        shopper_element = self._create_shopper_element(
            contact_info, credit_card, seller_shopper_id, client_ip)
        data = etree.tostring(shopper_element)

        response, body = self.request('POST', self.shoppers_path, data=data)

        # Extract shopper id from location header
        new_shopper_url = urlparse(response.headers['location'])
        shopper_id = self.shopper_id_path_pattern.match(new_shopper_url.path).group(1)

        return shopper_id

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

        response, _ = self.request('PUT', self.shopper_path.format(shopper_id=shopper_id), data=data)
        return response.status_code == requests.codes.no_content


class Order(Resource):
    path = '/services/2/orders'

    def create(self, shopper_id, sku_id, amount_in_pence, credit_card=None,
               description=None, client_ip=None):
        """
        :type shopper_id: int or str
        :type sku_id: int or str
        :type amount_in_pence: int
        :type credit_card: models.CreditCardSelection
        :param description: Order description
        :return:
        """
        # noinspection PyPep8Naming
        E = self.client.E

        amount = '{:.2f}'.format(amount_in_pence / 100.0)

        order = []
        if description is not None:
            order.append(getattr(E, 'soft-descriptor')(description))

        ordering_shopper = []
        if credit_card is not None:
            ordering_shopper.append(credit_card.to_xml())

        order_element = E.order(
            getattr(E, 'ordering-shopper')(
                getattr(E, 'shopper-id')(str(shopper_id)),
                models.WebInfo(ip=client_ip).to_xml(),
                *ordering_shopper
            ),
            E.cart(
                getattr(E, 'cart-item')(
                    E.sku(
                        getattr(E, 'sku-id')(str(sku_id)),
                        getattr(E, 'sku-charge-price')(
                            getattr(E, 'charge-type')('initial'),
                            E.amount(amount),
                            E.currency(self.client.currency)
                        )
                    ),
                    E.quantity('1'),
                ),
            ),
            getattr(E, 'expected-total-price')(
                E.amount(amount),
                E.currency(self.client.currency)
            ),
            *order
        )

        response, body = self.request('POST', self.path, data=etree.tostring(order_element))
        return body['order']
