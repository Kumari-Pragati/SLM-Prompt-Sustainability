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

    def test_edge_cases(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path"))
        self.assertTrue(is_valid_URL("https://www.example.com/path"))
        self.assertFalse(is_valid_URL("http://www.example.com/path/"))

    def test_special_characters(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path?query"))
        self.assertTrue(is_valid_URL("https://www.example.com/path?query"))

    def test_port_number(self):
        self.assertTrue(is_valid_URL("http://www.example.com:80"))
        self.assertTrue(is_valid_URL("https://www.example.com:443"))
