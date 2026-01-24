import unittest
from338_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_SubstringWithEqualEnds(""), 0)

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(count_SubstringWithEqualEnds(char), 1)

    def test_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds("radar"), 3)
        self.assertEqual(count_SubstringWithEqualEnds("level"), 2)
        self.assertEqual(count_SubstringWithEqualEnds("racecar"), 5)

    def test_non_palindrome_with_equal_ends(self):
        self.assertEqual(count_SubstringWithEqualEnds("ababa"), 2)
        self.assertEqual(count_SubstringWithEqualEnds("ababcd"), 1)

    def test_non_palindrome_with_different_ends(self):
        self.assertEqual(count_SubstringWithEqualEnds("abcd"), 0)
        self.assertEqual(count_SubstringWithEqualEnds("abcdefg"), 0)

    def test_long_string(self):
        long_string = 'a' * 1000 + 'z' * 1000
        self.assertEqual(count_SubstringWithEqualEnds(long_string), 2000)
