import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Repeat("abcd"), ["a", "b", "c", "d"])
        self.assertEqual(Repeat("a"), ["a"])
        self.assertEqual(Repeat("aa"), ["a"])
        self.assertEqual(Repeat("aaa"), ["a"])

    def test_edge_case(self):
        self.assertEqual(Repeat(""), [])
        self.assertEqual(Repeat("a "), ["a"])
        self.assertEqual(Repeat("ab"), ["a", "b"])
        self.assertEqual(Repeat("abc"), ["a", "b", "c"])
        self.assertEqual(Repeat("abcdabcd"), ["a", "b", "c", "d"])
        self.assertEqual(Repeat("abcdabcdabcd"), ["a", "b", "c", "d"])

    def test_corner_case(self):
        self.assertEqual(Repeat("aaabbb"), ["a", "b"])
        self.assertEqual(Repeat("abab"), ["a", "b"])
        self.assertEqual(Repeat("ababab"), ["a", "b"])
        self.assertEqual(Repeat("abababab"), ["a", "b"])
