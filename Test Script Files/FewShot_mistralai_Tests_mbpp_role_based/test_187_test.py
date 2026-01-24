import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(longest_common_subsequence("", ""), 0)
        self.assertEqual(longest_common_subsequence("", "ABC"), 0)
        self.assertEqual(longest_common_subsequence("ABC", ""), 0)

    def test_single_char_strings(self):
        self.assertEqual(longest_common_subsequence("A", "A"), 1)
        self.assertEqual(longest_common_subsequence("A", "B"), 0)
        self.assertEqual(longest_common_subsequence("B", "A"), 0)

    def test_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE"), 2)
        self.assertEqual(longest_common_subsequence("ABCDEFG", "ABC"), 3)
        self.assertEqual(longest_common_subsequence("ABCDEFG", "ABCDEF"), 6)

    def test_different_lengths(self):
        self.assertEqual(longest_common_subsequence("ABC", "DEF"), 0)
        self.assertEqual(longest_common_subsequence("ABC", "AB"), 2)
        self.assertEqual(longest_common_subsequence("AB", "ABC"), 2)
