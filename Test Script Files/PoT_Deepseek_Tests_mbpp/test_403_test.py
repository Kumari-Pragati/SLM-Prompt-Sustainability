import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))

    def test_edge_cases(self):
        self.assertFalse(is_valid_URL("httpx://www.example.com"))
        self.assertFalse(is_valid_URL("http:/www.example.com"))
        self.assertFalse(is_valid_URL("http://"))
        self.assertFalse(is_valid_URL(""))

    def test_corner_cases(self):
        self.assertFalse(is_valid_URL("http://www.example.com/path/to/resource?query=param#fragment"))
        self.assertFalse(is_valid_URL("http://www.example.com/path/to/resource?query=param#fragment"))
        self.assertFalse(is_valid_URL("http://www.example.com/path/to/resource?query=param#fragment"))
        self.assertFalse(is_valid_URL("http://www.example.com/path/to/resource?query=param#fragment"))
