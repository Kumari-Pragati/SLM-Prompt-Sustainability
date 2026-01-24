import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)

    def test_string_with_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_string_with_one_equal_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_string_with_multiple_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_string_with_no_equal_ends_and_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a b c"), 0)

    def test_string_with_spaces_and_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a b a"), 2)

    def test_string_with_no_equal_ends_and_punctuation(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a, b! c"), 0)

    def test_string_with_punctuation_and_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a, b! a"), 1)
