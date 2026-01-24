import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_permutation_of_same_length(self):
        self.assertTrue(check_permutation("abc", "cab"))
        self.assertTrue(check_permutation("ABC", "CBA"))

    def test_permutation_of_different_lengths(self):
        self.assertFalse(check_permutation("abc", "abcd"))
        self.assertFalse(check_permutation("ABC", "ABCD"))

    def test_empty_strings(self):
        self.assertTrue(check_permutation("", ""))

    def test_single_character_strings(self):
        self.assertTrue(check_permutation("a", "a"))
        self.assertFalse(check_permutation("a", "b"))

    def test_case_insensitive(self):
        self.assertTrue(check_permutation("abc", "ABC"))
        self.assertTrue(check_permutation("ABC", "abc"))
