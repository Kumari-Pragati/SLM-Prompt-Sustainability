import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):
    def test_typical_url(self):
        self.assertTrue(is_valid_URL('http://www.example.com'))
        self.assertTrue(is_valid_URL('https://www.example.com'))

    def test_url_without_www(self):
        self.assertTrue(is_valid_URL('http://example.com'))
        self.assertTrue(is_valid_URL('https://example.com'))

    def test_url_with_path(self):
        self.assertTrue(is_valid_URL('http://www.example.com/path'))
        self.assertTrue(is_valid_URL('https://www.example.com/path'))

    def test_url_with_query_string(self):
        self.assertTrue(is_valid_URL('http://www.example.com?query=string'))
        self.assertTrue(is_valid_URL('https://www.example.com?query=string'))

    def test_url_with_fragment_identifier(self):
        self.assertTrue(is_valid_URL('http://www.example.com#fragment'))
        self.assertTrue(is_valid_URL('https://www.example.com#fragment'))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL('httpx://www.example.com'))
        self.assertFalse(is_valid_URL('http:/www.example.com'))
        self.assertFalse(is_valid_URL('http:/example.com'))
        self.assertFalse(is_valid_URL('http://'))
        self.assertFalse(is_valid_URL(''))
        self.assertFalse(is_valid_URL(None))
