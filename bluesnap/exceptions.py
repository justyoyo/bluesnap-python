import re


class APIError(Exception):
    def __init__(self, messages, status_code):
        self.messages = messages
        self.status_code = status_code

    def __str__(self):
        suffix = " (HTTP status code was {status_code})".format(status_code=self.status_code)

        if isinstance(self.messages, str) or isinstance(self.messages, unicode):
            return self.messages + suffix
        else:
            import json
            return json.dumps(self.messages, indent=2) + suffix


class CardError(Exception):
    simple_description_matcher = re.compile(
        'Order creation could not be completed because of payment processing failure: \d+ - (.*)')

    def __init__(self, code, description):
        self.code = code
        self.description = description

        # Extract simple description
        try:
            self.simple_description = self.simple_description_matcher.match(description).group(1)
        except IndexError:
            self.simple_description = description

    def __str__(self):
        return '{description} (BlueSnap error code was {code})'.format(
            code=self.code,
            description=self.description)


class ImproperlyConfigured(Exception):
    pass


class ValidationError(Exception):
    pass
