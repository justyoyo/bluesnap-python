from base64 import b64encode
from functools import wraps
import re

import responses
import xmltodict

from bluesnap import client


shoppers = {}


def _assert_request_authorized(client, request):
    assert request.headers['content-type'] == 'application/xml'

    # Check authorization header
    assert request.headers['authorization'] == ('Basic %s' % b64encode(
        '%s:%s' % (client.username, client.password)))


def _add_callbacks():
    _client = client.default()

    def assert_authorized(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            _assert_request_authorized(
                client=_client,
                request=request)
            return func(request, *args, **kwargs)
        return wrapper

    @assert_authorized
    def create_shopper_callback(request):
        body = xmltodict.parse(request.body)
        shopper_info = body['shopper']['shopper-info']

        # Check client configuration
        assert shopper_info['store-id'] == _client.default_store_id
        assert shopper_info['shopper-currency'] == _client.default_currency
        assert shopper_info['locale'] == _client.locale

        new_shopper_id = max(shoppers.keys() or [0]) + 1

        shopper_info['shopper-id'] = new_shopper_id
        shopper_info['username'] = 'username_%d' % new_shopper_id
        shopper_info['password'] = 'password_%d' % new_shopper_id
        shopper_info['shipping-contact-info'] = None
        shopper_info['invoice-contacts-info'] = {
            'invoice-contact-info': dict(
                default=True,
                **shopper_info['shopper-contact-info']
            ),
        }
        shopper_info['payment-info'] = {
            'credit-cards-info': {
                'credit-card-info': [],
            },
            'ecps-info': None,
            'balance': None,
        }

        shoppers[new_shopper_id] = body

        # print xmltodict.unparse(body)
        # import json; print json.dumps(body, indent=4)

        headers = {
            'location': '%s/services/2/shoppers/%d' % (_client.endpoint_url, 1),
        }
        return (201, headers, '')

    @assert_authorized
    def get_shopper_callback(request):
        _assert_request_authorized(client=_client, request=request)

        try:
            raw_shopper_id = request.path_url.split('/')[-1]
            shopper_id = int(raw_shopper_id)
            shopper = shoppers[shopper_id]
        except (KeyError, ValueError):
            return (404, {},
                    'User: %s is not authorized to view shopper: %s.' % (
                        _client.username, shopper_id))
        else:
            return (200, {}, xmltodict.unparse(shopper))

    @assert_authorized
    def put_shopper_callback(request):
        _assert_request_authorized(client=_client, request=request)

        try:
            raw_shopper_id = request.path_url.split('/')[-1]
            shopper_id = int(raw_shopper_id)
            shopper = shoppers[shopper_id]
        except (KeyError, ValueError):
            return (404, {},
                    'User: %s is not authorized to view shopper: %s.' % (
                        _client.username, shopper_id))
        else:
            body = xmltodict.parse(request.body)
            payment_info = body['shopper']['shopper-info']['payment-info']
            credit_card = payment_info['credit-cards-info'][
                'credit-card-info']['credit-card']
            credit_card['card-last-four-digits'] = credit_card[
                'card-number'][-4:]

            for key in credit_card.keys():
                if key not in ('card-type', 'card-last-four-digits'):
                    del credit_card[key]

            # Update shopper
            credit_card_info = shopper['shopper']['shopper-info'][
                'payment-info']['credit-cards-info']['credit-card-info']
            credit_card_info.append(
                payment_info['credit-cards-info']['credit-card-info'])

            return (204, {}, '')

    responses.add_callback(
        responses.POST,
        '%s/services/2/shoppers' % _client.endpoint_url,
        callback=create_shopper_callback)
    responses.add_callback(
        responses.GET,
        re.compile(r'%s/services/2/shoppers/\d+' % _client.endpoint_url),
        callback=get_shopper_callback)
    responses.add_callback(
        responses.PUT,
        re.compile(r'%s/services/2/shoppers/\d+' % _client.endpoint_url),
        callback=put_shopper_callback)


def activate(func):
    """Mock api activation wrapper"""
    @wraps(func)
    @responses.activate
    def wrapper(*args, **kwargs):
        _add_callbacks()
        return func(*args, **kwargs)
    return wrapper
