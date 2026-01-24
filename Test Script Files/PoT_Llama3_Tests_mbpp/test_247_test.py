import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(lps("abab"), 4)
        self.assertEqual(lps("aba"), 3)
        self.assertEqual(lps("abc"), 1)
        self.assertEqual(lps("abaaba"), 6)
        self.assertEqual(lps("ababab"), 6)

    def test_edge(self):
        self.assertEqual(lps(""), 0)
        self.assertEqual(lps("a"), 1)
        self.assertEqual(lps("aa"), 2)
        self.assertEqual(lps("aaa"), 3)
        self.assertEqual(lps("aaaa"), 4)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            lps(None)
        with self.assertRaises(TypeError):
            lps(123)
