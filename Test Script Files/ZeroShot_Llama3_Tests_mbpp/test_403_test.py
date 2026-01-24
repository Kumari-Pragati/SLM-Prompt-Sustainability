import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL("example.com"))
        self.assertFalse(is_valid_URL("http://"))
        self.assertFalse(is_valid_URL("https://"))
        self.assertFalse(is_valid_URL(None))

    def test_url_with_query_string(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path?a=1&b=2"))
        self.assertTrue(is_valid_URL("https://www.example.com/path?a=1&b=2"))

    def test_url_with_fragment(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path#a=1"))
        self.assertTrue(is_valid_URL("https://www.example.com/path#a=1"))

    def test_url_with_port(self):
        self.assertTrue(is_valid_URL("http://www.example.com:80"))
        self.assertTrue(is_valid_URL("https://www.example.com:443"))

    def test_url_with_subdomain(self):
        self.assertTrue(is_valid_URL("http://subdomain.example.com"))
        self.assertTrue(is_valid_URL("https://subdomain.example.com"))
