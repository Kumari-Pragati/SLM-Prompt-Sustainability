import unittest
from mbpp_30_code import count_Substring_With_Equal_Ends

class TestCountSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            self.assertEqual(count_Substring_With_Equal_Ends(char), 1)

    def test_palindrome(self):
        self.assertEqual(count_Substring_With_Equal_Ends("racecar"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("level"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("madam"), 2)

    def test_non_palindrome(self):
        self.assertEqual(count_Substring_With_Equal_Ends("hello"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("python"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"), 0)
