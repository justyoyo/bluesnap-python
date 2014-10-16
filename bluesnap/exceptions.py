import re


class APIError(Exception):
    """
    If description is passed, messages would be ignored
    """
    def __init__(self, messages=None, description=None, code=None, status_code=None):
        self.messages = messages
        self.description = str(description)
        self.code = code
        self.status_code = status_code

    def __str__(self):
        if self.description is not None:
            string = self.description
        else:
            if isinstance(self.messages, str) or isinstance(self.messages, unicode):
                string = self.messages
            else:
                import json
                string = json.dumps(self.messages, indent=2)

        if self.code is not None:
            string += ' (BlueSnap error code was {0})'.format(self.code)

        if self.status_code is not None:
            string += ' (HTTP status code was {status_code})'.format(status_code=self.status_code)

        return string


class CardError(Exception):
    simple_description_matcher = re.compile(
        'Order creation could not be completed because of payment processing failure: \d+ - (.*)')

    def __init__(self, description, code=None, status_code=None):
        self.verbose_description = description
        self.code = code
        self.status_code = status_code

        # Extract simple description
        try:
            self.description = self.simple_description_matcher.match(self.verbose_description).group(1)
        except IndexError:
            self.description = self.verbose_description

    def __str__(self):
        string = self.description

        if self.code is not None:
            string += ' (BlueSnap error code was {0})'.format(self.code)

        if self.status_code is not None:
            string += ' (HTTP status code was {status_code})'.format(status_code=self.status_code)

        return string


class ImproperlyConfigured(Exception):
    pass


class ValidationError(Exception):
    pass
