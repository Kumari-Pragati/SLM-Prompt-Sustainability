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
        self.assertFalse(is_valid_URL("example"))
        self.assertFalse(is_valid_URL("http://example"))
        self.assertFalse(is_valid_URL("http://example.com@"))
        self.assertFalse(is_valid_URL("http://example.com.com"))
        self.assertFalse(is_valid_URL("http://example.com.123"))
        self.assertFalse(is_valid_URL("http://example.com.12345678901234567890"))
        self.assertFalse(is_valid_URL("http://example.com.123456789012345678901234567890"))
        self.assertFalse(is_valid_URL("http://example.com/"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/too/many/slashes"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/no/slashes"))
        self.assertFalse(is_valid_URL("http://example.com:8080"))
        self.assertFalse(is_valid_URL("http://example.com:80"))
        self.assertFalse(is_valid_URL("http://example.com:8080/"))
        self.assertFalse(is_valid_URL("http://example.com:8080/path/with/slashes"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/special_characters!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))
        self.assertFalse(is_valid_URL("http://example.com/path/with/only_special_characters!@#$%^&*()_+-=[]{}|;:'\",.<>/?"))
