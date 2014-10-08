from .schema import shopper as shopper_schema


class Resource(object):
    pass


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

        raise Exception
