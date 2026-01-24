import unittest
from187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(longest_common_subsequence("", "", 0, 0), 0)

    def test_single_char_strings(self):
        self.assertEqual(longest_common_subsequence("A", "", 1, 0), 0)
        self.assertEqual(longest_common_subsequence("", "A", 0, 1), 0)
        self.assertEqual(longest_common_subsequence("A", "A", 1, 1), 1)

    def test_simple_strings(self):
        self.assertEqual(longest_common_subsequence("ABCD", "AC", 4, 2), 2)
        self.assertEqual(longest_common_subsequence("AC", "ABCD", 2, 4), 2)
        self.assertEqual(longest_common_subsequence("ABCD", "ABCE", 4, 5), 1)
        self.assertEqual(longest_common_subsequence("ABCE", "ABCD", 5, 4), 1)

    def test_repeated_chars(self):
        self.assertEqual(longest_common_subsequence("AA", "BB", 2, 2), 2)
        self.assertEqual(longest_common_subsequence("AA", "A", 2, 1), 1)
        self.assertEqual(longest_common_subsequence("A", "AA", 1, 2), 1)

    def test_edge_cases(self):
        self.assertEqual(longest_common_subsequence("ABCDEFG", "ABC", 7, 3), 3)
        self.assertEqual(longest_common_subsequence("ABC", "ABCDEFG", 3, 7), 3)
        self.assertEqual(longest_common_subsequence("ABCDEFG", "", 7, 0), 0)
        self.assertEqual(longest_common_subsequence("", "ABCDEFG", 0, 7), 0)
