import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(string_to_list("Hello World"), ["Hello", "World"])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ["Hello", "World"])

    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_to_list("Hello World   "), ["Hello", "World"])

    def test_string_with_leading_spaces(self):
        self.assertEqual(string_to_list("   Hello World"), ["Hello", "World"])

    def test_string_with_special_characters(self):
        self.assertEqual(string_to_list("Hello@World"), ["Hello@World"])

    def test_string_with_numbers(self):
        self.assertEqual(string_to_list("Hello123World"), ["Hello123World"])

    def test_string_with_mixed_case(self):
        self.assertEqual(string_to_list("Hello WoRlD"), ["Hello", "WoRlD"])
