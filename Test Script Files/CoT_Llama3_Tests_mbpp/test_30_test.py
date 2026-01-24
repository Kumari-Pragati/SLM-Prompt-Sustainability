import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_string_with_no_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_string_with_one_substring_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 1)

    def test_string_with_multiple_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 2)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 1)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends_2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 2)

    def test_string_with_substrings_with_equal_ends_and_non_equal_ends_3(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abababa"), 2)
