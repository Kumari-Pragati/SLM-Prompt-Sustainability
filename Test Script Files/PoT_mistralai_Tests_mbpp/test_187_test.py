import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 4, 4), 2)
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB", 7, 8), 4)
        self.assertEqual(longest_common_subsequence("SIFTS", "SIFTST", 5, 6), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(longest_common_subsequence("", "AB", 0, 2), 0)
        self.assertEqual(longest_common_subsequence("AB", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)
        self.assertEqual(longest_common_subsequence("AB", "A", 1, 1), 0)
        self.assertEqual(longest_common_subsequence("AB", "AB", 1, 2), 1)
        self.assertEqual(longest_common_subsequence("AB", "ABC", 1, 3), 0)
        self.assertEqual(longest_common_subsequence("ABC", "AB", 2, 1), 0)
        self.assertEqual(longest_common_subsequence("ABC", "ABC", 2, 2), 2)
        self.assertEqual(longest_common_subsequence("ABC", "ABCD", 2, 3), 1)
