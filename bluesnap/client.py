from requests.auth import HTTPBasicAuth
import logging
import requests


class Client(object):
    ENDPOINTS = {
        'live': 'https://ws.bluesnap.com',
        'sandbox': 'https://sandbox.bluesnap.com'
    }

    def __init__(self,
                 # Environment
                 env,
                 # Authentication
                 username, password,
                 # Default store Id
                 default_store_id):
        if env not in self.ENDPOINTS:
            raise ValueError('env not in {0}'.format(self.ENDPOINTS.keys()))

        self.env = env
        self.username = username
        self.password = password
        self.default_store_id = default_store_id

    @property
    def endpoint_url(self):
        return self.ENDPOINTS[self.env]

    def _get_http_basic_auth(self):
        return HTTPBasicAuth(self.username, self.password)

    # def request(self, method, url, ):
