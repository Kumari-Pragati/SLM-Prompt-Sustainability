import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(lps(""), 0)

    def test_single_character_string(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEqual(lps(char), 1)

    def test_palindromes(self):
        self.assertEqual(lps("A"), 1)
        self.assertEqual(lps("AA"), 2)
        self.assertEqual(lps("AABA"), 4)
        self.assertEqual(lps("AABBA"), 6)
        self.assertEqual(lps("AABBAA"), 7)
        self.assertEqual(lps("AABBBAA"), 9)

    def test_non_palindromes(self):
        self.assertEqual(lps("ABC"), 2)
        self.assertEqual(lps("ABCA"), 3)
        self.assertEqual(lps("ABCBA"), 5)
        self.assertEqual(lps("ABCBBAC"), 7)
        self.assertEqual(lps("ABCBBACA"), 8)
