import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_edge_case_single_character_string_with_same_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 3)

    def test_edge_case_single_character_string_with_different_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)

    def test_edge_case_long_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_edge_case_long_string_with_repeated_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aabbccdd"), 6)

    def test_edge_case_long_string_with_repeated_characters_and_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aabbccdd  "), 6)

    def test_edge_case_long_string_with_repeated_characters_and_spaces_and_punctuation(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aabbccdd !"), 6)
