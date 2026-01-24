import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(lps('a'), 1)

    def test_same_characters(self):
        self.assertEqual(lps('aaaa'), 4)

    def test_different_characters(self):
        self.assertEqual(lps('abcd'), 1)

    def test_palindrome(self):
        self.assertEqual(lps('abba'), 4)

    def test_empty_string(self):
        self.assertEqual(lps(''), 0)

    def test_long_string(self):
        self.assertEqual(lps('abcddcba'), 7)

    def test_long_palindrome(self):
        self.assertEqual(lps('abcddcbaabcddcba'), 14)

    def test_long_different_characters(self):
        self.assertEqual(lps('abcdefghijklmnopqrstuvwxyz'), 1)
