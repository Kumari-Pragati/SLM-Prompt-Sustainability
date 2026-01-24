import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(lps("abcd"), 3)
        self.assertEqual(lps("abab"), 2)
        self.assertEqual(lps("abcdefg"), 6)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)

    def test_edge_cases(self):
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("a "), 1)
        self.assertEqual(lps(" abc "), 1)
        self.assertEqual(lps("abcdabcd"), 4)

    def test_corner_cases(self):
        self.assertEqual(lps("aabb"), 2)
        self.assertEqual(lps("abba"), 2)
        self.assertEqual(lps("abbaabba"), 4)
        self.assertEqual(lps("aabbabba"), 3)
