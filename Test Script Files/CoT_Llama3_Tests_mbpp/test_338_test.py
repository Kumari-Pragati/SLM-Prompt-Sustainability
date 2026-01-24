import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_string_with_no_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_string_with_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 2)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends_and_no_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends_and_no_substrings_and_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends_and_no_substrings_and_single_character_and_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
