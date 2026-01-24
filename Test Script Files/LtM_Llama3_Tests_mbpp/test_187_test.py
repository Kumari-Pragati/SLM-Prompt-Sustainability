import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)

    def test_single_character_strings(self):
        self.assertEqual(longest_common_subsequence("a", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "a", 0, 1), 0)
        self.assertEqual(longest_common_subsequence("a", "a", 1, 1), 1)

    def test_short_strings(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)
        self.assertEqual(longest_common_subsequence("abc", "abcd", 3, 4), 1)

    def test_long_strings(self):
        self.assertEqual(longest_common_subsequence("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26, 26), 26)
        self.assertEqual(longest_common_subsequence("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz123", 26, 27), 26)

    def test_edge_cases(self):
        self.assertEqual(longest_common_subsequence("a", "b", 1, 1), 0)
        self.assertEqual(longest_common_subsequence("a", "a", 1, 1), 1)
        self.assertEqual(longest_common_subsequence("", "a", 0, 1), 0)
        self.assertEqual(longest_common_subsequence("a", "", 1, 0), 0)
