import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lps("abcba"), 5)
        self.assertEqual(lps("aaaa"), 4)
        self.assertEqual(lps("abcdeedcba"), 9)

    def test_edge_cases(self):
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("ab"), 1)
        self.assertEqual(lps("aaa"), 3)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            lps(12345)
        with self.assertRaises(TypeError):
            lps(None)
        with self.assertRaises(TypeError):
            lps(123.45)
