import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(string_list_to_tuple(["hello", " ", "world"]), ("hello", "world"))

    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_list_with_only_spaces(self):
        self.assertEqual(string_list_to_tuple([" ", "  ", "   "]), ())

    def test_list_with_only_non_space_chars(self):
        self.assertEqual(string_list_to_tuple(["hello", "world"]), ("hello", "world"))

    def test_list_with_mixed_spaces_and_non_space_chars(self):
        self.assertEqual(string_list_to_tuple(["hello", " ", "world"]), ("hello", "world"))

    def test_list_with_duplicates(self):
        self.assertEqual(string_list_to_tuple(["hello", " ", "world", " ", "hello"]), ("hello", "world", "hello"))
