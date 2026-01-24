import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 4, 4), 2)
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB", 7, 8), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(longest_common_subsequence("", "AB", 0, 2), 0)
        self.assertEqual(longest_common_subsequence("AB", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)
        self.assertEqual(longest_common_subsequence("AB", "AB", 1, 1), 1)
        self.assertEqual(longest_common_subsequence("AB", "ABC", 1, 2), 0)
        self.assertEqual(longest_common_subsequence("ABC", "AB", 2, 1), 0)

    def test_special_or_corner_cases(self):
        self.assertEqual(longest_common_subsequence("A", "A", 1, 1), 1)
        self.assertEqual(longest_common_subsequence("AA", "AA", 2, 2), 2)
        self.assertEqual(longest_common_subsequence("ABC", "CBA", 3, 2), 2)
        self.assertEqual(longest_common_subsequence("ABC", "ABCA", 3, 4), 3)
        self.assertEqual(longest_common_subsequence("ABC", "ABCC", 3, 4), 2)
