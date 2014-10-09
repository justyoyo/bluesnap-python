from urlparse import urlparse
import platform

from lxml import objectify, etree
import requests

from .client import default as default_client
from .version import __version__


class Resource(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""


class Shopper(Resource):
    path = '/services/2/shoppers'

    def create(self):
        # <shopper/>
        shopper = objectify.Element('shopper', nsmap={None: 'http://ws.plimus.com'})
        shopper['Merchant-shopper-id'] = '123456'  # Not implemented

        shopper_info = objectify.SubElement(shopper, 'shopper-info')
        # shopper_info.username = 'user_123'
        shopper_info['store-id'] = self.client.default_store_id
        shopper_info['shopper-currency'] = 'GBP'
        shopper_info['locale'] = 'en'

        shopper_contact_info = objectify.SubElement(shopper_info, 'shopper-contact-info')
        shopper_contact_info['first-name'] = 'John'
        shopper_contact_info['last-name'] = 'Doe'
        shopper_contact_info['email'] = 'test@justyoyo.com'
        shopper_contact_info['address1'] = '(Empty)'
        shopper_contact_info['city'] = '(Empty)'
        shopper_contact_info['zip'] = 'SW5'
        shopper_contact_info['country'] = 'gb'
        shopper_contact_info['phone'] = '07777777777'

        # payment_info = objectify.SubElement(shopper_info, 'payment-info')
        # credit_card_info = objectify.SubElement(payment_info, 'credit-card-info')
        # credit_card = objectify.SubElement(credit_card_info, 'credit-card')
        # credit_card['encrypted-card-number'] = '$bsjs_0_0_1$E/KfuDDrO2qlQourN27HFVRWKWut4B7djNvPpEua88rj0+Z6wYBkD1Bk7v6A12srVHSgoj8/N9M281C6N3RxwgNT3kWnDeY34nn/gfJ1ZMw1+mRtWKW/GBKm2zumqP+BUnys2MlHJrfq41XqeY0QiPMxBy5pTcXR7gwmxTOy6IEzsNBCfdn9nyZI1XWI3VEZFxkKjse7JUPYXI6z8Xci169I3eIaZfAk/VWMRdEyE4BjWymdedCnI4ZPtLQEXtMcq96Qpg0vwAyYBtR6txlAotaVDIyNXqVzt+/lbdNXnV1Qa3btgBxaeu9WiKpCnjjOedZFsbt3GH8GC+y1+NFkdQ==$3BcXsd1u2zmXJ5bu1JE5dvcclsMTnrBb9lJ8/yUgYdV8pVJ3Df1DrlQouqxBuVLq$oiIo1MykCjuHYHDaY5tqdhguf7WTetosGpQis40SvAU='
        # credit_card['card-type'] = 'VISA'
        # credit_card['expiration-month'] = '10'
        # credit_card['expiration-year'] = '2014'
        # credit_card['encrypted-security-code'] = '$bsjs_0_0_1$f6obJCCjXf4evUIZVW+QxggcvR0bAO9W8oAOF5TKIu6JbSVDHF34WTS9SeBtsJ5JpXnlkxKCCRF7I8s4812PzlUXi6wCf5MkzwYW0oRsDXdZ/fwJNwn9pWOpPEVVAdfmITOEQsbKgBsb3rAW1tUvVqDo7KF3tVpthEE610ohF3SZ4h9spiA+KNEeIPUDXgfmyQoVWrpofqnBpx0vpKjALnFS/7qMyzQE1F1o7k/dhFxbVyMLUmnUVBQqsgEGi9C3JSskwjioBL9ZpWjv65ss8etXHpvQEz4KaNN3YxxeDNBckGaMLJxUx3AGsr3eOWqi9WJ/rHjfFapnvBMAqoHmsg==$JUGQgq/g9gGsq731irqCwb4A+omDjPOu2uB4PzAsRv8=$+rcTMubbGnNqsCjAY1QSr4NITwTAoiR+woddYptCyX0='

        web_info = objectify.SubElement(shopper, 'web-info')
        web_info['ip'] = '1.1.1.1'

        library_versions = 'requests {}; python {}'.format(requests.__version__, platform.version())
        web_info['user-agent'] = 'justyoyo/bluesnap-python {} ({})'.format(__version__, library_versions)

        xml = etree.tostring(shopper, pretty_print=True)
        print xml

        # shopper_contact_info = shopper_schema.shopper_contact_info(
        #     first_name='first name'
        # )
        # shopper_contact_info.build()
        # shopper_contact_info.first_name = 'First name'

        # shopper_info = shopper_schema.shopper_info()
        # shopper_info.shopper_contact_info = shopper_contact_info

        # shopper.shopper_info = shopper_info


        # print shopper.toString()
        # shopper = shopper_schema.shopper()
        #
        # shopper_contact_info = shopper_schema.shopper_contact_info()
        # shopper_contact_info.first_name = 'First name'
        # shopper_contact_info.last_name = 'Last name'
        # shopper_contact_info.email = 'test@example.com'
        #
        # shopper_info = shopper_schema.shopper_info()
        # shopper_info.shopper_contact_info = shopper_contact_info
        #
        # shopper.shopper_info = shopper_info
        #
        # print shopper.toxml('utf-8')
        # # print type(shopper.__class__)
        #
        r = self.client.request('POST', self.path, data=xml)

        if r.status_code == requests.codes.created:
            new_shopper_url = urlparse(r.headers['location'])

            r = self.client.request('GET', new_shopper_url.path)
            shopper = etree.XML(r.content)
            print etree.tostring(shopper, pretty_print=True)
        else:
            print 'here', r.text

            messages = etree.XML(r.content)

            for message in messages:
                print 'ok'
                print etree.tostring(message, pretty_print=True)
                # data = {}
                # for attr in message.iter():
                #     data[attr.tag] = attr.text

                # print data
                # print message.findtext('{*}code')
                # print message.findtext('{*}description')
                # if hasattr(message, 'description'):
                #     print message.description

            # print dir(messages), messages.__class__

            # for message in messages.message:
            #     print message

            # print etree.tostring(messages, pretty_print=True)

            #
            # print messages_schema.CreateFromDocument(r.text)

        raise Exception
