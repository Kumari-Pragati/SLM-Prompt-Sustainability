import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(longest_common_subsequence("ABCD", "AC", 4, 2), 1)
        self.assertEqual(longest_common_subsequence("ABCD", "AC", 2, 4), 0)
        self.assertEqual(longest_common_subsequence("ABCD", "AB", 4, 2), 2)
        self.assertEqual(longest_common_subsequence("ABCD", "AB", 2, 4), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)
        self.assertEqual(longest_common_subsequence("A", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "A", 0, 1), 0)
        self.assertEqual(longest_common_subsequence("A", "AB", 1, 2), 1)
        self.assertEqual(longest_common_subsequence("AB", "A", 2, 1), 0)

    def test_complex(self):
        self.assertEqual(longest_common_subsequence("ABCBDAB", "ABCAB", 7, 5), 4)
        self.assertEqual(longest_common_subsequence("ABCBDAB", "ABCAB", 5, 7), 4)
        self.assertEqual(longest_common_subsequence("ABCBDAB", "ABCAB", 0, 7), 0)
        self.assertEqual(longest_common_subsequence("ABCBDAB", "ABCAB", 7, 0), 0)
