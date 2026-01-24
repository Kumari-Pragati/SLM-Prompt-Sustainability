import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(lps("ababcbab"), 5)
        self.assertEqual(lps("aababcd"), 4)
        self.assertEqual(lps("abcdabcd"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)
        self.assertEqual(lps("aaa"), 3)
        self.assertEqual(lps("abababab"), 7)
        self.assertEqual(lps("ababababab"), 8)

    def test_special_cases(self):
        self.assertEqual(lps("abba"), 3)
        self.assertEqual(lps("abab"), 2)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)
        self.assertEqual(lps("aaa"), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, lps, 123)
        self.assertRaises(TypeError, lps, [])
