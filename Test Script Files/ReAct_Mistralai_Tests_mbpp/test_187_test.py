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
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 4, 4), 1)
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 4, 3), 1)
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 3, 4), 1)
        self.assertEqual(longest_common_subsequence("ABCD", "ACDE", 3, 3), 2)

    def test_overlapping_strings(self):
        self.assertEqual(longest_common_subsequence("ABC", "CBA", 3, 3), 2)
        self.assertEqual(longest_common_subsequence("ABC", "CAB", 3, 3), 2)
        self.assertEqual(longest_common_subsequence("ABC", "BAC", 3, 3), 1)

    def test_error_handling(self):
        with self.assertRaises(IndexError):
            longest_common_subsequence("ABC", "CBA", 4, 4)
        with self.assertRaises(IndexError):
            longest_common_subsequence("ABC", "CBA", -1, 3)
        with self.assertRaises(TypeError):
            longest_common_subsequence(1, 2, 3, 4)
