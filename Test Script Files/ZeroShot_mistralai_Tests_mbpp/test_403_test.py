import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.org"))
        self.assertTrue(is_valid_URL("http://www.example.net"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL("example.com"))
        self.assertFalse(is_valid_URL("http://example"))
        self.assertFalse(is_valid_URL("http://example.com@example.org"))
        self.assertFalse(is_valid_URL("http://example.com/?query"))
        self.assertFalse(is_valid_URL("http://example.com#fragment"))
        self.assertFalse(is_valid_URL("example.com.example"))
        self.assertFalse(is_valid_URL("http://-example.com"))
        self.assertFalse(is_valid_URL("http://example.com/./"))
        self.assertFalse(is_valid_URL("http://example.com/../"))
