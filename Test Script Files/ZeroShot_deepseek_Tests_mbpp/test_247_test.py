import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_lps(self):
        self.assertEqual(lps("abba"), 4)
        self.assertEqual(lps("abcba"), 5)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("abababab"), 4)
        self.assertEqual(lps("aaaa"), 4)
        self.assertEqual(lps("abcabcabc"), 3)
        self.assertEqual(lps("abcd"), 1)
        self.assertEqual(lps("abcda"), 2)
        self.assertEqual(lps("abcde"), 1)
