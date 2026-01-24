import unittest
from mbpp_247_code import lps

class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character(self):
        for char in "ABC":
            self.assertEqual(lps(char), 1)

    def test_palindromes(self):
        self.assertEqual(lps("racecar"), 6)
        self.assertEqual(lps("level"), 5)
        self.assertEqual(lps("radar"), 4)
        self.assertEqual(lps("amanaplanacanalpanama"), 15)

    def test_edge_cases(self):
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)
        self.assertEqual(lps("ab"), 1)
        self.assertEqual(lps("abb"), 2)
        self.assertEqual(lps("abbab"), 3)
        self.assertEqual(lps("aabbaba"), 5)

    def test_non_palindromes(self):
        self.assertEqual(lps("cat"), 1)
        self.assertEqual(lps("catdog"), 2)
        self.assertEqual(lps("hello world"), 1)
