import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(string_list_to_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))

    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_list_with_spaces(self):
        self.assertEqual(string_list_to_tuple(['a ', ' b', ' c ']), ('a', 'b', 'c'))

    def test_list_with_empty_strings(self):
        self.assertEqual(string_list_to_tuple(['', 'a', '']), ('a',))

    def test_list_with_whitespace_only(self):
        self.assertEqual(string_list_to_tuple([' ', '   ', '']), ())

    def test_list_with_mixed_whitespace_and_non_whitespace(self):
        self.assertEqual(string_list_to_tuple(['a ', 'b', '  c']), ('a', 'b', 'c'))
