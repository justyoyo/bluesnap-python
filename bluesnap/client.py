from pyexpat import ExpatError
from lxml.builder import ElementMaker
from requests.auth import HTTPBasicAuth
import requests
import xmltodict
from logging import Logger
from exceptions import ImproperlyConfigured, ValidationError, APIError, CardError


def default_user_agent():
    """
    Generate default user agent based on library repo name, Python version and requests version
    :return: string
    """
    import platform
    from .version import __version__
    library_versions = 'requests {}; python {}'.format(requests.__version__, platform.version())
    return 'justyoyo/bluesnap-python {} ({})'.format(__version__, library_versions)


class Client(object):
    ENDPOINTS = {
        'live': 'https://ws.bluesnap.com',
        'sandbox': 'https://sandbox.bluesnap.com'
    }

    NAMESPACE = 'http://ws.plimus.com'

    # List of error codes that is considered a card error
    CARD_ERROR_CODES = {'14002'}

    def __init__(self,
                 # Environment
                 env,
                 # Authentication
                 username, password,
                 # Default store Id
                 default_store_id,
                 # Seller id
                 seller_id,
                 # Default currency
                 default_currency,
                 # Locale
                 locale='en',
                 # Logger
                 logger=None):
        if env not in self.ENDPOINTS:
            raise ValueError('env not in {0}'.format(self.ENDPOINTS.keys()))

        self.env = env
        self.username = username
        self.password = password
        self.default_store_id = default_store_id
        self.seller_id = seller_id
        self.default_currency = default_currency.upper()
        self.locale = locale

        self.logger = logger if isinstance(logger, Logger) else None

        # ElementMaker for XML builder
        self.E = ElementMaker(namespace=self.NAMESPACE,
                              nsmap={None: self.NAMESPACE})

    @property
    def endpoint_url(self):
        return self.ENDPOINTS[self.env]

    @property
    def http_basic_auth(self):
        return HTTPBasicAuth(self.username, self.password)

    @property
    def currency(self):
        # TODO ability to change this in the future
        return self.default_currency

    @property
    def store_id(self):
        # TODO ability to change this in the future
        return str(self.default_store_id)

    def request(self, method, path, data=None):
        """
        API request method

        :param method: HTTP method
        :param path: URL path
        :param data: XML data
        :return:
        """
        headers = {
            'content-type': 'application/xml',  # Must be XML or API will complain
        }

        url = self.endpoint_url + path

        request = getattr(requests, method.lower())  # requests.{get,post,put,delete}

        if self.logger:
            self.logger.info(
                '\n\t'.join([
                    'Bluesnap request:',
                    method,
                    str(url),
                    str(headers),
                    str(data)]))

        response = request(url,
                           headers=headers,
                           auth=self.http_basic_auth,
                           data=data)

        if self.logger:
            self.logger.info(
                '\n\t'.join([
                    'Bluesnap response:',
                    'Code: %s' % str(response.status_code),
                    'Headers: %s' % str(dict(response.headers)),
                    'Content: %s' % response.content]))

        body = self._process_response_body(response)

        return response, body

    def _process_response_body(self, response):
        body = None

        if response.content:  # There's content, parse it as XML
            try:
                body = xmltodict.parse(response.content)
            except ExpatError:
                # Cannot parse body as XML, could be a text
                raise APIError(description=response.content, status_code=response.status_code)

        if not (200 <= response.status_code < 300):
            self._handle_api_error(response, body)

        return body

    # noinspection PyMethodMayBeStatic
    def _handle_api_error(self, response, body):
        """
        Try to find the error message and raise the correct exception
        :raises APIError
        :param response: HTTP response
        :param body: Messages may contain in <xml/> or <messages><message/></messages>
        """
        try:  # <xml>message</xml>
            if body:
                description = body['xml']
            else:
                description = '<no response body>'
            raise APIError(description=description,
                           status_code=response.status_code)
        except (KeyError, ValueError):
            try:  # <messages><message><description>message</description></message></messages>
                if isinstance(body['messages']['message'], list):  # Multiple <message/> elements
                    raise APIError(messages=body['messages']['message'],
                                   status_code=response.status_code)
                else:  # Only 1 <message/> element
                    code = body['messages']['message'].get('code', None)

                    if code is not None and code in self.CARD_ERROR_CODES:  # Found a CardError
                        klass = CardError
                    else:
                        klass = APIError

                    raise klass(description=body['messages']['message']['description'],
                                code=code,
                                status_code=response.status_code)

            except (KeyError, ValueError):  # I don't understand how to interpret this API error
                raise APIError(
                    description='Invalid messages object in response from API: {body}'.format(body=body),
                    status_code=response.status_code)

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
