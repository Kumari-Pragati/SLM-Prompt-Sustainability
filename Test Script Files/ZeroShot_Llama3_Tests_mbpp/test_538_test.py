import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_string_list_to_tuple(self):
        self.assertEqual(string_list_to_tuple("Hello World"), ("Hello", "World"))
        self.assertEqual(string_list_to_tuple("   "), ())
        self.assertEqual(string_list_to_tuple("   Hello   "), ("Hello",))
        self.assertEqual(string_list_to_tuple("Hello, World!"), ("Hello,", "World!"))
        self.assertEqual(string_list_to_tuple(""), ())
        self.assertEqual(string_list_to_tuple("   Hello   World   "), ("Hello", "World"))

    def test_string_list_to_tuple_empty_string(self):
        self.assertEqual(string_list_to_tuple(""), ())

    def test_string_list_to_tuple_single_space(self):
        self.assertEqual(string_list_to_tuple("   "), ())

    def test_string_list_to_tuple_multiple_spaces(self):
        self.assertEqual(string_list_to_tuple("   Hello   World   "), ("Hello", "World"))

    def test_string_list_to_tuple_multiple_spaces_and_comma(self):
        self.assertEqual(string_list_to_tuple("   Hello, World!   "), ("Hello,", "World!"))
