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
        self.assertEqual(longest_common_subsequence("abc", "abcd", 3, 4), 1)
        self.assertEqual(longest_common_subsequence("abcd", "abc", 4, 3), 1)

    def test_long_strings(self):
        self.assertEqual(longest_common_subsequence("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26, 26), 26)

    def test_disjoint_strings(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)

    def test_identical_strings(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_identical_subsequence(self):
        self.assertEqual(longest_common_subsequence("abc", "abc", 3, 3), 3)

    def test_subsequence_at_end(self):
        self.assertEqual(longest_common_subsequence("abc", "defabc", 3, 7), 3)

    def test_subsequence_at_start(self):
        self.assertEqual(longest_common_subsequence("abc", "abcde", 3, 5), 3)

    def test_subsequence_in_middle(self):
        self.assertEqual(longest_common_subsequence("abcde", "abcde", 5, 5), 3)
