import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_equal_strings(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_diff_length_strings(self):
        self.assertFalse(check_permutation("abc", "abcd"))

    def test_permutation_strings(self):
        self.assertTrue(check_permutation("abc", "bac"))

    def test_non_permutation_strings(self):
        self.assertFalse(check_permutation("abc", "def"))

    def test_empty_string(self):
        self.assertTrue(check_permutation("", ""))

    def test_single_char_strings(self):
        self.assertTrue(check_permutation("a", "a"))

    def test_empty_string_with_non_empty(self):
        self.assertFalse(check_permutation("", "abc"))
