import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_edge_case_single_character_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 1)

    def test_edge_case_multiple_character_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)

    def test_edge_case_multiple_character_string_without_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_edge_case_string_with_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a b c"), 0)

    def test_edge_case_string_with_punctuation(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a,b,c"), 0)

    def test_edge_case_string_with_numbers(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a1b2c3"), 0)

    def test_edge_case_string_with_special_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a!b@c"), 0)
