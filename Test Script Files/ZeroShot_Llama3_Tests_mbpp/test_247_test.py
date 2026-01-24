import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_lps(self):
        self.assertEqual(lps("ab"), 1)
        self.assertEqual(lps("aba"), 2)
        self.assertEqual(lps("abba"), 4)
        self.assertEqual(lps("abc"), 1)
        self.assertEqual(lps("abcd"), 1)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("aabb"), 4)
        self.assertEqual(lps("aabbcc"), 6)
        self.assertEqual(lps("aabbccdd"), 8)

    def test_lps_edge_cases(self):
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps(""), 0)
