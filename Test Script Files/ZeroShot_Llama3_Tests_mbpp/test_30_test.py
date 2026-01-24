import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_single_character_substring(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)

    def test_multiple_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)

    def test_no_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_substrings_with_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)
