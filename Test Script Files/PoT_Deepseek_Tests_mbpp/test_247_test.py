import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lps("abba"), 4)
        self.assertEqual(lps("abcba"), 5)
        self.assertEqual(lps("racecar"), 7)

    def test_edge_cases(self):
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps(""), 0)

    def test_boundary_cases(self):
        self.assertEqual(lps("abababab"), 8)
        self.assertEqual(lps("aaaaaaa"), 7)

    def test_corner_cases(self):
        self.assertEqual(lps("abcdefg"), 1)
        self.assertEqual(lps("ggggggg"), 7)
