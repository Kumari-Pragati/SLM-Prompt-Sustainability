import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_typical_url(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))

    def test_url_without_www(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))

    def test_url_without_protocol(self):
        self.assertFalse(is_valid_URL("www.example.com"))

    def test_url_with_special_characters(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path?query=param"))
        self.assertTrue(is_valid_URL("https://www.example.com/path?query=param"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL("httpx://www.example.com"))
        self.assertFalse(is_valid_URL("http:/www.example.com"))
        self.assertFalse(is_valid_URL("http:/example.com"))
        self.assertFalse(is_valid_URL("http//example.com"))
        self.assertFalse(is_valid_URL("http:/"))
        self.assertFalse(is_valid_URL(""))
        self.assertFalse(is_valid_URL(None))
