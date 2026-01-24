import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_single_character_string_with_same_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 2)

    def test_single_character_string_with_different_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 1)

    def test_multiple_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 2)

    def test_multiple_character_string_with_same_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcba"), 4)

    def test_multiple_character_string_with_different_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 2)

    def test_string_with_repeated_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 4)

    def test_string_with_repeated_substrings_and_same_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abababab"), 6)

    def test_string_with_repeated_substrings_and_different_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdabcd"), 4)
