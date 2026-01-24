import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(number_of_substrings("abc"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_edge_case_single_char_string(self):
        self.assertEqual(number_of_substrings("a"), 1)

    def test_edge_case_two_char_string(self):
        self.assertEqual(number_of_substrings("ab"), 2)

    def test_edge_case_long_string(self):
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            number_of_substrings(123)
