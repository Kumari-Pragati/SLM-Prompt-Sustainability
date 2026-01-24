import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)

    def test_edge_case1(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_edge_case2(self):
        self.assertEqual(longest_common_subsequence("abc", "", 3, 0), 0)

    def test_edge_case3(self):
        self.assertEqual(longest_common_subsequence("", "abc", 0, 3), 0)

    def test_edge_case4(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)

    def test_edge_case5(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_edge_case6(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)

    def test_edge_case7(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_edge_case8(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)

    def test_edge_case9(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_edge_case10(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)
