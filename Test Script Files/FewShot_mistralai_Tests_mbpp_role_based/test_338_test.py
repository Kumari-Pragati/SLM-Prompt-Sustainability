import unittest
from mbpp_338_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_SubstringWithEqualEnds(""), 0)

    def test_single_character_string(self):
        for char in range(ord('a'), ord('z') + 1):
            self.assertEqual(count_SubstringWithEqualEnds(chr(char)), 1)

    def test_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds("radar"), 1)
        self.assertEqual(count_SubstringWithEqualEnds("level"), 1)

    def test_non_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds("abcdefg"), 0)
        self.assertEqual(count_SubstringWithEqualEnds("xyz"), 0)

    def test_mixed_case(self):
        self.assertEqual(count_SubstringWithEqualEnds("RaDaR"), 1)
        self.assertEqual(count_SubstringWithEqualEnds("LeVeL"), 1)

    def test_long_string(self):
        self.assertEqual(count_SubstringWithEqualEnds("abcdefghijklmnopqrstuvwxyz"), 1)
