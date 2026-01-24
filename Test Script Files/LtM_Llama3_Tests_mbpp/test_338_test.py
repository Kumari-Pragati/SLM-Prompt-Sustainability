import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_single_character_string_with_duplicates(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 2)

    def test_string_with_no_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_string_with_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_string_with_substrings_with_equal_ends_and_duplicates(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 4)

    def test_string_with_substrings_with_equal_ends_and_duplicates_with_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab ab"), 2)

    def test_string_with_substrings_with_equal_ends_and_duplicates_with_spaces_and_punctuation(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab. ab"), 2)
