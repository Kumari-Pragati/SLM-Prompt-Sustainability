import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):
    def test_valid_URL(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))

    def test_invalid_URL(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL(""))

    def test_edge_cases(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path"))
        self.assertTrue(is_valid_URL("https://www.example.com/path"))
        self.assertFalse(is_valid_URL("http://example.com/path/"))

    def test_invalid_URLs(self):
        self.assertFalse(is_valid_URL("ftp://example.com"))
        self.assertFalse(is_valid_URL("example.com"))
        self.assertFalse(is_valid_URL("http://example.com/path/"))
