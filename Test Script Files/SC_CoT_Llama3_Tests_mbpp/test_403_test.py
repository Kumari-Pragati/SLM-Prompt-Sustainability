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
        self.assertFalse(is_valid_URL("http://"))
        self.assertFalse(is_valid_URL("https://"))
        self.assertFalse(is_valid_URL("example.com"))
        self.assertFalse(is_valid_URL("http://example"))
        self.assertFalse(is_valid_URL("https://example"))

    def test_edge_cases(self):
        self.assertFalse(is_valid_URL("http://www.example.com/"))
        self.assertFalse(is_valid_URL("https://www.example.com/"))
        self.assertFalse(is_valid_URL("http://example.com/"))
        self.assertFalse(is_valid_URL("https://example.com/"))

    def test_special_cases(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path"))
        self.assertTrue(is_valid_URL("https://www.example.com/path"))
        self.assertTrue(is_valid_URL("http://example.com/path"))
        self.assertTrue(is_valid_URL("https://example.com/path"))
