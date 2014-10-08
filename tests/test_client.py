import unittest

from bluesnap.client import BluesnapClient


class BluesnapClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = BluesnapClient()

