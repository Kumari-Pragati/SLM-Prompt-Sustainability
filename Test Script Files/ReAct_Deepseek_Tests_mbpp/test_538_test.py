import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_list_to_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))

    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_list_with_spaces(self):
        self.assertEqual(string_list_to_tuple(['a ', ' b', ' c ']), ('a', 'b', 'c'))

    def test_list_with_whitespace_only(self):
        self.assertEqual(string_list_to_tuple([' ', '   ', '']), ())

    def test_list_with_mixed_characters(self):
        self.assertEqual(string_list_to_tuple(['a', 'b', 'c', '']), ('a', 'b', 'c'))

    def test_list_with_numbers(self):
        self.assertEqual(string_list_to_tuple(['1', '2', '3']), ('1', '2', '3'))
