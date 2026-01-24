import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(common_prefix([ "flower", "flow", "flight" ], 3), "fl")
        self.assertEqual(common_prefix([ "dog", "racecar", "car" ], 3), "")
        self.assertEqual(common_prefix([ "apple", "apples", "apricot" ], 3), "app")

    def test_edge_cases(self):
        self.assertEqual(common_prefix([], 0), "")
        self.assertEqual(common_prefix([ "a" ], 1), "a")
        self.assertEqual(common_prefix([ "aa", "a" ], 2), "a")
        self.assertEqual(common_prefix([ "aa", "a", "b" ], 3), "")

    def test_complex(self):
        self.assertEqual(common_prefix([ "abcd", "abcef", "abcdef" ], 3), "abc")
        self.assertEqual(common_prefix([ "abc", "abcd", "abcd", "abcdabcd" ], 4), "abcd")
        self.assertEqual(common_prefix([ "z", "y", "x", "w" ], 4), "")
