import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)

    def test_single_character_strings(self):
        self.assertEqual(longest_common_subsequence("a", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "a", 0, 1), 0)
        self.assertEqual(longest_common_subsequence("a", "a", 1, 1), 1)

    def test_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("abc", "def", 3, 3), 0)
        self.assertEqual(longest_common_subsequence("abc", "bdf", 3, 3), 1)
        self.assertEqual(longest_common_subsequence("abc", "abcd", 3, 4), 1)
        self.assertEqual(longest_common_subsequence("abc", "defg", 3, 4), 0)

    def test_no_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("abc", "defgh", 3, 5), 0)
        self.assertEqual(longest_common_subsequence("abcd", "efgh", 4, 4), 0)

    def test_empty_string(self):
        self.assertEqual(longest_common_subsequence("abc", "", 3, 0), 0)
        self.assertEqual(longest_common_subsequence("", "def", 0, 3), 0)

    def test_single_character_strings(self):
        self.assertEqual(longest_common_subsequence("a", "b", 1, 1), 0)
        self.assertEqual(longest_common_subsequence("a", "a", 1, 1), 1)
