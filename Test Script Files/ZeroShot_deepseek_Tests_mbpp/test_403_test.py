import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://www.google.com"))
        self.assertTrue(is_valid_URL("https://www.python.org"))
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://www.example.com"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_URL("htt://www.google.com"))
        self.assertFalse(is_valid_URL("http:/www.google.com"))
        self.assertFalse(is_valid_URL("http://google"))
        self.assertFalse(is_valid_URL("http://www.google."))
        self.assertFalse(is_valid_URL("http://www.google.com/path"))
        self.assertFalse(is_valid_URL("http://www.google.com:8080"))
        self.assertFalse(is_valid_URL("http://user:password@www.google.com"))
        self.assertFalse(is_valid_URL("http://www.google.com?query=string"))
        self.assertFalse(is_valid_URL("http://www.google.com#fragment"))
        self.assertFalse(is_valid_URL("http://www.google.com:8080/path?query=string#fragment"))
        self.assertFalse(is_valid_URL("http://user:password@www.google.com:8080/path?query=string#fragment"))

    def test_none_url(self):
        self.assertFalse(is_valid_URL(None))
