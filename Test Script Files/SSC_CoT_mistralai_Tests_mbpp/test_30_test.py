import unittest
from mbpp_30_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_WithEqualEnds(""), 0)

    def test_single_character(self):
        for char in range(ord('a'), ord('z') + 1):
            self.assertEqual(count_Substring_WithEqualEnds(chr(char)), 1)

    def test_palindrome(self):
        self.assertEqual(count_Substring_WithEqualEnds("radar"), 3)
        self.assertEqual(count_Substring_WithEqualEnds("level"), 2)
        self.assertEqual(count_Substring_WithEqualEnds("racecar"), 4)

    def test_non_palindrome(self):
        self.assertEqual(count_Substring_WithEqualEnds("abcdefg"), 0)
        self.assertEqual(count_Substring_WithEqualEnds("hello"), 0)
        self.assertEqual(count_Substring_WithEqualEnds("python"), 0)

    def test_long_string(self):
        long_string = "a" * 1000
        self.assertEqual(count_Substring_WithEqualEnds(long_string), 1000)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_Substring_WithEqualEnds, 123)
        self.assertRaises(TypeError, count_Substring_WithEqualEnds, [])
