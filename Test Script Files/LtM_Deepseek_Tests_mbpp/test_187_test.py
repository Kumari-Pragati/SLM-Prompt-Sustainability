import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(longest_common_subsequence("ABCDGH", "AEDFHR", 6, 6), 3)
        self.assertEqual(longest_common_subsequence("ABC", "ABC", 3, 3), 3)

    def test_edge_conditions(self):
        self.assertEqual(longest_common_subsequence("", "ABC", 0, 3), 0)
        self.assertEqual(longest_common_subsequence("ABC", "", 3, 0), 0)
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)

    def test_complex_cases(self):
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB", 6, 7), 4)
        self.assertEqual(longest_common_subsequence("ABCDEF", "ABDCEF", 6, 6), 6)
