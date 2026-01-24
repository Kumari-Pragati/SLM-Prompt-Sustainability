import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lps("abba"), 4)
        self.assertEqual(lps("abcba"), 5)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps(""), 0)

    def test_edge_cases(self):
        self.assertEqual(lps("aaaaa"), 5)
        self.assertEqual(lps("abababab"), 4)

    def test_corner_cases(self):
        self.assertEqual(lps("abcdcba"), 7)
        self.assertEqual(lps("abcddcba"), 7)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lps(123)
        with self.assertRaises(TypeError):
            lps(None)
        with self.assertRaises(TypeError):
            lps(123456)
        with self.assertRaises(TypeError):
            lps(["ab", "cd"])
