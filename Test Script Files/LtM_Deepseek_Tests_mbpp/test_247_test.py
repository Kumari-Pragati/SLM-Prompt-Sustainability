import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_simple_palindrome(self):
        self.assertEqual(lps("abcba"), 5)

    def test_typical_palindrome(self):
        self.assertEqual(lps("racecar"), 7)

    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character(self):
        self.assertEqual(lps("a"), 1)

    def test_palindrome_with_duplicates(self):
        self.assertEqual(lps("aabaa"), 5)

    def test_non_palindrome(self):
        self.assertEqual(lps("abcd"), 1)

    def test_long_palindrome(self):
        self.assertEqual(lps("abccba"), 6)
