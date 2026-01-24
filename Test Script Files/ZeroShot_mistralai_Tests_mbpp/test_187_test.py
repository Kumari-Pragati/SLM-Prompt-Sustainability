import unittest
from mbpp_187_code import longest_common_subsequence

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

    def test_complex_strings(self):
        self.assertEqual(longest_common_subsequence("Sunday", "Monday", 5, 6), 4)
        self.assertEqual(longest_common_subsequence("Monday", "Sunday", 6, 5), 4)
        self.assertEqual(longest_common_subsequence("Mississippi", "Appalachia", 11, 9), 5)
        self.assertEqual(longest_common_subsequence("Appalachia", "Mississippi", 9, 11), 5)
