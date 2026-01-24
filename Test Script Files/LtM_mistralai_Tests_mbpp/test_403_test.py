import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):
    def test_simple_valid_urls(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.org"))
        self.assertTrue(is_valid_URL("http://www.example.net"))

    def test_edge_cases(self):
        self.assertTrue(is_valid_URL("https://example.com."))
        self.assertTrue(is_valid_URL("http://example.com:8080"))
        self.assertTrue(is_valid_URL("https://example.com/path/with/slashes"))
        self.assertTrue(is_valid_URL("http://example.com?query=string"))
        self.assertTrue(is_valid_URL("https://example.com#anchor"))

    def test_invalid_inputs(self):
        self.assertFalse(is_valid_URL(None))
        self.assertFalse(is_valid_URL(""))
        self.assertFalse(is_valid_URL("example"))
        self.assertFalse(is_valid_URL("http://example.com example.com"))
        self.assertFalse(is_valid_URL("http://example.com@example.com"))
        self.assertFalse(is_valid_URL("http://example.com/example"))
        self.assertFalse(is_valid_URL("http://example.com/example.com"))
        self.assertFalse(is_valid_URL("http://example.com/example.com/"))
        self.assertFalse(is_valid_URL("http://example.com/example.com#"))
