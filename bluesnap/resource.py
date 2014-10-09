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

    def create_root_element(self, tag):
        return objectify.Element(tag, nsmap=self.client.XML_NAMESPACES)


class Shopper(Resource):
    path = '/services/2/shoppers'

    def create(self):
        # /shopper
        shopper = self.create_root_element('shopper')

        # /shopper/shopper-info
        shopper_info = objectify.SubElement(shopper, 'shopper-info')
        # shopper_info.username = 'user_123'
        shopper_info['store-id'] = self.client.default_store_id
        shopper_info['shopper-currency'] = 'GBP'
        shopper_info['locale'] = 'en'

        # shopper_info['seller-shopper-id'] = '1234'  # Our user id

        # /shopper/shopper-info/shopper-contact-info
        shopper_contact_info = objectify.SubElement(shopper_info, 'shopper-contact-info')
        shopper_contact_info['first-name'] = 'John'
        shopper_contact_info['last-name'] = 'Doe'
        shopper_contact_info['email'] = 'test@justyoyo.com'
        shopper_contact_info['address1'] = '(Empty)'
        shopper_contact_info['city'] = '(Empty)'
        shopper_contact_info['zip'] = 'SW5'
        shopper_contact_info['country'] = 'gb'
        shopper_contact_info['phone'] = '07777777777'

        # /shopper/shopper-info/payment-info
        payment_info = objectify.SubElement(shopper_info, 'payment-info')

        # /shopper/shopper-info/payment-info/credit-cards-info
        credit_cards_info = objectify.SubElement(payment_info, 'credit-cards-info')

        # /shopper/shopper-info/payment-info/credit-cards-info/credit-card-info
        credit_card_info = objectify.SubElement(credit_cards_info, 'credit-card-info')

        # /shopper/shopper-info/payment-info/credit-cards-info/credit-card-info/billing-contact-info
        billing_contact_info = objectify.SubElement(credit_card_info, 'billing-contact-info')
        billing_contact_info['first-name'] = 'John'
        billing_contact_info['last-name'] = 'Doe'
        billing_contact_info['email'] = 'test@justyoyo.com'
        billing_contact_info['address1'] = '(Empty)'
        billing_contact_info['city'] = '(Empty)'
        billing_contact_info['zip'] = 'SW5'
        billing_contact_info['country'] = 'gb'
        billing_contact_info['phone'] = '07777777777'

        # /shopper/shopper-info/payment-info/credit-cards-info/credit-card-info/credit-card
        credit_card = objectify.SubElement(credit_card_info, 'credit-card')
        credit_card['card-type'] = 'VISA'
        credit_card['expiration-month'] = '10'
        credit_card['expiration-year'] = '2014'
        credit_card['card-number'] = '4111111111111111'
        credit_card['security-code'] = '123'
        # credit_card['encrypted-card-number'] = r'$bsjs_0_0_1$fcFSIszGd/zeff2ykDptFvIVK5fsLxZpVmH1bujSYBfRwqRGvHbt/ig4BiSaCdnhqvFge/eMDcn6HMrzot4jNDxij70eEDUpoNI/ynhwlE7YEKfUPaax8OayU6SrAh1j5XlLAqHOXi9e0dfouy684uJP8l/nnnSAb6YsBFE+wTiSUJkuTCEbLdIxVPon7pfmPCiWFbq5ApTg2OoyBnHCEazAwNwFYb5rDi2clGZOrZ9t2aTiLMt8lI9eOxGK56B4VbMLEPFx9cC1k28mhl9ngEP8krM1hsmr60PtjbChBl76YGiIIkpO4oB4/B60mJ3yH9m7TCNVf6o+hAuhGPUPFA==$s9Gt7eXUdG3wnsCYXuylw8GEbPuHHtoc82wuDLlawiYj9Cz97C7X6VJ8Lr9SpPcX$0lkNKEuDWG6d9GVf3TWykyEePSfgAdqPPLgCV2JW7bQ='
        # credit_card['encrypted-security-code'] = r'$bsjs_0_0_1$WIZtg12e6eDuZ9lVIypJ5KZ0l81pHaSuIHvsavNowrcnvhmPzVGasjWMi9MxEAUPjoA+t/PKLTu1zuclcQQU9Qrrd/inOyb4JQdzu8V0f6bnl3b6r8n20c8hTY/SxDc2VTQUnprD4ue9xanHX+EeTDxBMAr7+EI9DvF6v/wGpJUzxi9EbxIA1I9yPtbXP+CnXlRCwOkIUxA2G4u178lSkEIN+2RO190be1imguBVuPh5V29/CeOjujk+3Wf6XcFjIbt5yN7WFYsrrY7XVWyTu9LXTto3HWihUAJXSt6y9Q3WuZ6cL+cYsqs6OmupmyPFsiStn7cWYJxcrst9/XsE1A==$J6AeBXHNoDQ84rq/1yNtZX5iPbbXlXBz0LxK3Vx8JZA=$lBpanoq9MuGmI7N/cpiVoO/ueF4JZm5ofrDVCj9Wvw0='

        # /shopper/web-info
        web_info = objectify.SubElement(shopper, 'web-info')
        web_info['ip'] = '1.1.1.1'

        library_versions = 'requests {}; python {}'.format(requests.__version__, platform.version())
        web_info['user-agent'] = 'justyoyo/bluesnap-python {} ({})'.format(__version__, library_versions)

        objectify.deannotate(shopper)
        # etree.cleanup_namespaces(shopper)

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


class Order(Resource):
    path = '/services/2/orders'

    def create(self):
        # /order
        order = self.create_root_element('order')

