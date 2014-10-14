from pyexpat import ExpatError
from lxml.builder import ElementMaker
from requests.auth import HTTPBasicAuth
import requests
import xmltodict

from exceptions import ImproperlyConfigured, ValidationError


class Client(object):
    ENDPOINTS = {
        'live': 'https://ws.bluesnap.com',
        'sandbox': 'https://sandbox.bluesnap.com'
    }

    NAMESPACE = 'http://ws.plimus.com'

    def __init__(self,
                 # Environment
                 env,
                 # Authentication
                 username, password,
                 # Default store Id
                 default_store_id,
                 # Seller id
                 seller_id):
        if env not in self.ENDPOINTS:
            raise ValueError('env not in {0}'.format(self.ENDPOINTS.keys()))

        self.env = env
        self.username = username
        self.password = password
        self.default_store_id = default_store_id
        self.seller_id = seller_id

        # ElementMaker for XML builder
        self.E = ElementMaker(namespace=self.NAMESPACE,
                              nsmap={None: self.NAMESPACE})

    @property
    def endpoint_url(self):
        return self.ENDPOINTS[self.env]

    @property
    def http_basic_auth(self):
        return HTTPBasicAuth(self.username, self.password)

    def request(self, method, path, data=None):
        """
        :type method: str
        """
        headers = {
            'content-type': 'application/xml',  # Must be XML or API will complain
        }

        url = self.endpoint_url + path

        request = getattr(requests, method.lower())  # requests.{get,post,put,delete}

        response = request(url,
                           headers=headers,
                           auth=self.http_basic_auth,
                           data=data)

        if response.status_code in (requests.codes.ok, requests.codes.created):  # Everything is okay
            return response
        elif response.status_code == requests.codes.bad:  # Something bad happened
            try:
                messages = xmltodict.parse(response.content).get(u'messages', {}).get(u'message', [])
            except ExpatError:
                messages = response.body
            raise ValidationError(messages)
        else:  # Don't know how to handle this, so raise an error
            response.raise_for_status()


__client__ = None


def default():
    """:rtype : Client"""
    global __client__

    if __client__ is None:
        raise ImproperlyConfigured('BlueSnap client not configured yet. Please call bluesnap.client.configure().')

    return __client__


def configure(**config):
    """:rtype : Client"""
    global __client__

    __client__ = Client(**config)

    return __client__
