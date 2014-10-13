import platform

from lxml.builder import ElementMaker
from requests.auth import HTTPBasicAuth
import requests

from .version import __version__


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
            'content-type': 'application/xml',
        }

        url = self.endpoint_url + path

        request = getattr(requests, method.lower())  # requests.{get,post,put,delete}

        r = request(url,
                    headers=headers,
                    auth=self.http_basic_auth,
                    data=data)

        if r.status_code in (requests.codes.ok, requests.codes.created):
            # Everything is okay
            return r
        elif r.status_code == requests.codes.bad:
            return r
        else:
            # Don't know how to handle this
            r.raise_for_status()


__client__ = None


def default():
    """:rtype : Client"""
    global __client__

    if __client__ is None:
        # TODO refactor
        __client__ = Client(
            env='sandbox',
            username='username',
            password='password',
            default_store_id='1',
            seller_id='1'
        )

    return __client__


def configure(**config):
    """:rtype : Client"""
    global __client__
    __client__ = Client(**config)
    return __client__
