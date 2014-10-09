import datetime

now = datetime.datetime.now()
future = now + datetime.timedelta(days=1)

SANDBOX_CLIENT_CONFIG = {
    'env': 'sandbox',
    'username': 'API_14127729102161320867365',
    'password': 'JustYoyo1',
    'default_store_id': '13945'
}

# Dummy cards taken from
# http://home.bluesnap.com/integrationguide/default.htm#WordManual/Working_with_Sandbox_Testing.htm

DUMMY_CARD_VISA = {
    'number': '4111111111111111',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv2': '111'
}

DUMMY_CARD_MASTERCARD = {
    'number': '5105105105105100',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv2': '111'
}

DUMMY_CARD_AMEX = {
    'number': '378282246310005',
    'expire_month': future.month,
    'expire_year': future.year,
    'cvv2': '111'
}

DUMMY_CARDS = (
    ('Visa', DUMMY_CARD_VISA),
    ('MasterCard', DUMMY_CARD_MASTERCARD),
    ('American Express', DUMMY_CARD_AMEX)
)

