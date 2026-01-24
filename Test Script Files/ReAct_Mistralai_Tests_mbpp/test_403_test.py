import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_valid_url(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://www.example.org"))
        self.assertTrue(is_valid_URL("http://www.example.net"))

    def test_invalid_url_no_protocol(self):
        self.assertFalse(is_valid_URL("example.com"))
        self.assertFalse(is_valid_URL("www.example.org"))
        self.assertFalse(is_valid_URL("www.example.net"))

    def test_invalid_url_no_domain(self):
        self.assertFalse(is_valid_URL("http://"))
        self.assertFalse(is_valid_URL("https://"))
        self.assertFalse(is_valid_URL("http://."))
        self.assertFalse(is_valid_URL("https://."))

    def test_invalid_url_too_short(self):
        self.assertFalse(is_valid_URL("http"))
        self.assertFalse(is_valid_URL("https"))
        self.assertFalse(is_valid_URL("http."))
        self.assertFalse(is_valid_URL("https."))

    def test_invalid_url_too_long(self):
        self.assertFalse(is_valid_URL("http://a" * 257 + ".com"))
        self.assertFalse(is_valid_URL("https://a" * 257 + ".com"))
        self.assertFalse(is_valid_URL("http://a" * 257 + "."))
        self.assertFalse(is_valid_URL("https://a" * 257 + "."))

    def test_invalid_url_invalid_tld(self):
        self.assertFalse(is_valid_URL("http://example.comx"))
        self.assertFalse(is_valid_URL("https://example.orgx"))
        self.assertFalse(is_valid_URL("http://example.netx"))

    def test_invalid_url_special_characters(self):
        self.assertFalse(is_valid_URL("http://example.com/!@#$%^&*()_+-=[]{}|;':\"<>,.?/"))
        self.assertFalse(is_valid_URL("https://www.example.org/!@#$%^&*()_+-=[]{}|;':\"<>,.?/"))
        self.assertFalse(is_valid_URL("http://www.example.net/!@#$%^&*()_+-=[]{}|;':\"<>,.?/"))

    def test_invalid_url_empty_string(self):
        self.assertFalse(is_valid_URL(""))
