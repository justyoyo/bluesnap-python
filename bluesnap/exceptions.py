class APIError(Exception):
    def __init__(self, messages):
        self.messages = messages

    def __str__(self):
        if isinstance(self.messages, str) or isinstance(self.messages, unicode):
            return self.messages
        else:
            import json
            return json.dumps(self.messages, indent=2)


class ImproperlyConfigured(Exception):
    pass


class ValidationError(Exception):
    pass
