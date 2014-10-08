import requests

from .client import default as default_client
from .schema import shopper as shopper_schema


class Resource(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""


class Shopper(Resource):
    path = '/services/2/shoppers'

    def create(self):
        shopper = shopper_schema.shopper()

        shopper_contact_info = shopper_schema.shopper_contact_info()
        shopper_contact_info.first_name = 'First name'
        shopper_contact_info.last_name = 'Last name'
        shopper_contact_info.email = 'test@example.com'

        shopper_info = shopper_schema.shopper_info()
        shopper_info.shopper_contact_info = shopper_contact_info

        shopper.shopper_info = shopper_info

        print shopper.toxml('utf-8')
        # print type(shopper.__class__)

        r = self.client.request('POST', self.path, data=shopper.toxml('utf-8'))

        print r.text
        print repr(r)

        raise Exception
