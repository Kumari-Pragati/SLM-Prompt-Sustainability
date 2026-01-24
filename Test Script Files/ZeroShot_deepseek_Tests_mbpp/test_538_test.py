import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_list_to_tuple(""), ())

    def test_string_with_no_spaces(self):
        self.assertEqual(string_list_to_tuple("abc"), ('a', 'b', 'c'))

    def test_string_with_spaces(self):
        self.assertEqual(string_list_to_tuple("a b c"), ('a', 'b', 'c'))

    def test_string_with_multiple_spaces(self):
        self.assertEqual(string_list_to_tuple("a   b   c"), ('a', 'b', 'c'))

    def test_string_with_leading_spaces(self):
        self.assertEqual(string_list_to_tuple("   abc"), ('a', 'b', 'c'))

    def test_string_with_trailing_spaces(self):
        self.assertEqual(string_list_to_tuple("abc   "), ('a', 'b', 'c'))
