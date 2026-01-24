import unittest
from mbpp_403_code import is_valid_URL

class TestIsValidURL(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_valid_URL("http://www.example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))

    def test_typical_case_without_www(self):
        self.assertTrue(is_valid_URL("http://example.com"))
        self.assertTrue(is_valid_URL("https://example.com"))

    def test_typical_case_with_path(self):
        self.assertTrue(is_valid_URL("http://www.example.com/path"))
        self.assertTrue(is_valid_URL("https://example.com/path"))

    def test_typical_case_with_query_params(self):
        self.assertTrue(is_valid_URL("http://www.example.com?param=value"))
        self.assertTrue(is_valid_URL("https://example.com?param=value"))

    def test_typical_case_with_fragment(self):
        self.assertTrue(is_valid_URL("http://www.example.com#fragment"))
        self.assertTrue(is_valid_URL("https://example.com#fragment"))

    def test_edge_case_empty_string(self):
        self.assertFalse(is_valid_URL(""))

    def test_edge_case_none(self):
        self.assertFalse(is_valid_URL(None))

    def test_edge_case_invalid_url(self):
        self.assertFalse(is_valid_URL("invalid_url"))

    def test_edge_case_url_without_scheme(self):
        self.assertFalse(is_valid_URL("www.example.com"))

    def test_edge_case_url_with_invalid_characters(self):
        self.assertFalse(is_valid_URL("http://www.example.com/invalid%characters"))
