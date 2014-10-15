class APIError(Exception):
    def __init__(self, messages):
        self.messages = messages

    def __str__(self):
        import json
        return json.dumps(self.messages, indent=2)


class ImproperlyConfigured(Exception):
    pass


class ValidationError(Exception):
    pass
