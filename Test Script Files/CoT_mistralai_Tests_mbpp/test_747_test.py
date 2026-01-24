import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(lcs_of_three("", "", ""), 0)

    def test_single_char_strings(self):
        self.assertEqual(lcs_of_three("a", "", "a"), 1)
        self.assertEqual(lcs_of_three("", "a", "a"), 0)
        self.assertEqual(lcs_of_three("a", "b", "a"), 0)

    def test_identical_strings(self):
        self.assertEqual(lcs_of_three("abc", "abc", "abc"), 3)
        self.assertEqual(lcs_of_three("abc", "abcdef", "abc"), 3)
        self.assertEqual(lcs_of_three("abc", "abc", "abcdefg"), 0)

    def test_overlapping_longer_strings(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "abce"), 3)
        self.assertEqual(lcs_of_three("abc", "abcd", "abcde"), 3)
        self.assertEqual(lcs_of_three("abc", "abcd", "abcdef"), 3)

    def test_overlapping_shorter_strings(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "abc"), 3)
        self.assertEqual(lcs_of_three("abcd", "abc", "abc"), 3)
        self.assertEqual(lcs_of_three("abcd", "abc", "abce"), 3)

    def test_non_overlapping_longer_strings(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "abcf"), 2)
        self.assertEqual(lcs_of_three("abc", "abcd", "abcef"), 2)
        self.assertEqual(lcs_of_three("abc", "abcd", "abceg"), 2)

    def test_non_overlapping_shorter_strings(self):
        self.assertEqual(lcs_of_three("abc", "abcd", "abc"), 3)
        self.assertEqual(lcs_of_three("abcd", "abc", "abce"), 2)
        self.assertEqual(lcs_of_three("abcd", "abc", "abcf"), 2)

    def test_different_strings(self):
        self.assertEqual(lcs_of_three("abc", "def", "ghi"), 0)
        self.assertEqual(lcs_of_three("abc", "def", "abcdef"), 0)
        self.assertEqual(lcs_of_three("abc", "abcdef", "ghi"), 0)
