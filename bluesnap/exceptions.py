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


class ImproperlyConfigured(Exception):
    pass


class ValidationError(Exception):
    pass
