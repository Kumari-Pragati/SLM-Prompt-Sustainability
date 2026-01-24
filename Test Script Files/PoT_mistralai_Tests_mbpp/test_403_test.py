import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.org"))
        self.assertTrue(is_valid_URL("http://www.example.net"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL(""))
        self.assertFalse(is_valid_URL("http"))
        self.assertFalse(is_valid_URL("http://"))
        self.assertFalse(is_valid_URL("http://example"))
        self.assertFalse(is_valid_URL("http://example.com."))
        self.assertFalse(is_valid_URL("http://example.com@"))
        self.assertFalse(is_valid_URL("http://example.com#"))
        self.assertFalse(is_valid_URL("http://example.com?query"))
        self.assertFalse(is_valid_URL("http://example.com?query#fragment"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/slashes"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/long/path"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/very/very/very/very/long/path"))
