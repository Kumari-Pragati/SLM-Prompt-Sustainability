import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(Repeat("abcd"), ["a", "b", "c", "d"])
        self.assertEqual(Repeat("abc"), ["a", "b", "c"])
        self.assertEqual(Repeat("a"), ["a"])
        self.assertEqual(Repeat("aa"), ["a"])

    def test_edge_cases(self):
        self.assertEqual(Repeat(""), [])
        self.assertEqual(Repeat("aabb"), ["a", "b"])
        self.assertEqual(Repeat("aaa"), ["a"])
        self.assertEqual(Repeat("abab"), ["a", "b"])

    def test_complex(self):
        self.assertEqual(Repeat("ababcdabab"), ["a", "b", "d"])
        self.assertEqual(Repeat("aabbccaa"), ["a", "b", "c"])
        self.assertEqual(Repeat("aaabbbccc"), ["a", "b", "c"])
