import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_to_list("hello world"), ["hello", "world"])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(string_to_list("hello   world"), ["hello", "world"])

    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_to_list("hello world "), ["hello", "world"])

    def test_string_with_leading_spaces(self):
        self.assertEqual(string_to_list(" hello world"), ["hello", "world"])

    def test_special_characters(self):
        self.assertEqual(string_to_list("hello@world"), ["hello@world"])

    def test_numbers_in_string(self):
        self.assertEqual(string_to_list("123 456"), ["123", "456"])

    def test_empty_list_on_empty_string(self):
        self.assertEqual(string_to_list(""), [])
