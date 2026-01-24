import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(number_of_substrings("abc"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_of_substrings(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(number_of_substrings("a"), 1)

    def test_edge_case_empty_string_with_spaces(self):
        self.assertEqual(number_of_substrings("   "), 0)

    def test_edge_case_single_character_with_spaces(self):
        self.assertEqual(number_of_substrings(" a"), 1)

    def test_edge_case_multiple_characters(self):
        self.assertEqual(number_of_substrings("abcde"), 5)

    def test_edge_case_multiple_characters_with_spaces(self):
        self.assertEqual(number_of_substrings("a b c d e"), 5)

    def test_edge_case_long_string(self):
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_edge_case_long_string_with_spaces(self):
        self.assertEqual(number_of_substrings("a b c d e f g h i j k l m n o p q r s t u v w x y z"), 26)
