import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_string_with_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_string_with_multiple_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 3)

    def test_string_with_no_equal_ends_and_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc def"), 0)

    def test_string_with_equal_ends_and_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba cba"), 2)
