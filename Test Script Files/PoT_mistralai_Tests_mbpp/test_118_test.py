import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(string_to_list("hello world"), ["hello", "world"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(string_to_list(""), [])

    def test_edge_case_single_word(self):
        self.assertListEqual(string_to_list("example"), ["example"])

    def test_edge_case_whitespace_only(self):
        self.assertListEqual(string_to_list("   "), [""])

    def test_edge_case_leading_trailing_whitespace(self):
        self.assertListEqual(string_to_list("   hello   "), ["hello"])

    def test_edge_case_non_alphanumeric_characters(self):
        self.assertListEqual(string_to_list("!@#$%^&*()_+-=hello world"), ["!@#$%^&*()_+-=", "hello", "world"])
