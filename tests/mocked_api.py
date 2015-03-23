from base64 import b64encode
from functools import wraps
import re

import responses
import xmltodict

from . import helper
from bluesnap import client


def _assert_request_authorized(client, request):
    assert request.headers['content-type'] == 'application/xml'

    # Check authorization header
    assert request.headers['authorization'] == ('Basic %s' % b64encode(
        '%s:%s' % (client.username, client.password)))


mock_responses = {
    'card_expired': '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<messages
    xmlns="http://ws.plimus.com">
    <message>
        <error-name>EXPIRED_CARD</error-name>
        <code>14002</code>
        <description>Order creation could not be completed because of payment processing failure: 430306 - The expiration date entered is invalid. Enter valid expiration date or try another card</description>
    </message>
</messages>''',
    'insufficient_funds': '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<messages
    xmlns="http://ws.plimus.com">
    <message>
        <error-name>INSUFFICIENT_FUNDS</error-name>
        <code>14002</code>
        <description>Order creation could not be completed because of payment processing failure: 430360 - Insufficient funds. Please use another card or contact your bank for assistance</description>
    </message>
</messages>''',
    'invalid_card_number': '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<messages
    xmlns="http://ws.plimus.com">
    <message>
        <error-name>INVALID_CARD_NUMBER</error-name>
        <code>14002</code>
        <description>Order creation could not be completed because of payment processing failure: 430330 - Invalid card number. Please check the number and try again, or use a different card</description>
    </message>
</messages>''',
    'incorrect_information': '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<messages
    xmlns="http://ws.plimus.com">
    <message>
        <error-name>INCORRECT_INFORMATION</error-name>
        <code>14002</code>
        <description>Order creation could not be completed because of payment processing failure: 430285 - Authorization has failed for this transaction. Please try again or contact your bank for assistance</description>
    </message>
</messages>''',
}

def _generate_card_signature(card_number, expiration_month, expiration_year):
    return '%s/%d/%d' % (
        card_number, int(expiration_month), int(expiration_year))

credit_card_number_to_error_responses = {
    _generate_card_signature('4917484589897107', 4, 2018):
        mock_responses['card_expired'],
    _generate_card_signature('4917484589897107', 5, 2018):
        mock_responses['insufficient_funds'],
    _generate_card_signature('4917484589897107', 8, 2018):
        mock_responses['invalid_card_number'],
    _generate_card_signature('378282246310005', 5, 2018):
        mock_responses['incorrect_information'],
}


def _add_callbacks(shoppers):
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

            card_number = None

            # Attempt to extract credit card number
            if 'card-number' in credit_card:
                card_number = credit_card['card-number']
            elif ('encrypted-card-number' in credit_card
                    and credit_card['encrypted-card-number'].startswith(
                        'encrypted_')):
                card_number = credit_card['encrypted-card-number'][10:]

            # Check if invalid card numbers were used
            card_signature = _generate_card_signature(
                card_number=card_number,
                expiration_month=credit_card['expiration-month'],
                expiration_year=credit_card['expiration-year'])
            if card_signature in credit_card_number_to_error_responses:
                return (400,
                        {'content-type': 'application/xml'},
                        credit_card_number_to_error_responses[card_signature])

            credit_card['card-last-four-digits'] = card_number[-4:]

            # Remove unexpected fields
            keys_to_keep = {'card-type', 'card-last-four-digits'}
            for key_to_discard in (set(credit_card.keys()) - keys_to_keep):
                del credit_card[key_to_discard]

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
        shoppers = {}
        _add_callbacks(shoppers=shoppers)
        return func(*args, **kwargs)
    return wrapper
