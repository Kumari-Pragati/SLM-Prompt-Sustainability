import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertEqual(string_list_to_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))

    def test_empty_input(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_input_with_spaces(self):
        self.assertEqual(string_list_to_tuple(['a ', ' b', ' c ']), ('a', 'b', 'c'))

    def test_input_with_only_spaces(self):
        self.assertEqual(string_list_to_tuple(['   ', '    ', '     ']), ())

    def test_input_with_mixed_spaces_and_characters(self):
        self.assertEqual(string_list_to_tuple(['a ', '  b', ' c']), ('a', 'b', 'c'))
