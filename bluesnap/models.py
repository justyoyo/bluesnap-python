from collections import namedtuple


__all__ = ['ContactInfo', 'CreditCard']

ContactInfo = namedtuple('ContactInfo',
                         ['first_name', 'last_name', 'email', 'address_1', 'city', 'zip', 'country', 'phone'])

PlaintextCreditCard = namedtuple('PlaintextCreditCard',
                                 ['card_type', 'expiration_month', 'expiration_year', 'card_number', 'security_code'])

EncryptedCreditCard = namedtuple('EncryptedCreditCard',
                                 ['card_type', 'expiration_month', 'expiration_year', 'encrypted_card_number',
                                  'encrypted_security_code'])
