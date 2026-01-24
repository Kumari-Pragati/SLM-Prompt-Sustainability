import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_identical_strings(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_reversed_strings(self):
        self.assertTrue(check_permutation("abc", "cba"))

    def test_case_sensitivity(self):
        self.assertFalse(check_permutation("abc", "ABC"))

    def test_empty_strings(self):
        self.assertTrue(check_permutation("", ""))
        self.assertFalse(check_permutation("", "a"))

    def test_single_character_strings(self):
        self.assertTrue(check_permutation("a", "a"))
        self.assertFalse(check_permutation("a", "b"))

    def test_one_longer_than_other(self):
        self.assertFalse(check_permutation("abc", "abcd"))
        self.assertFalse(check_permutation("abcd", "abc"))

    def test_duplicate_characters(self):
        self.assertTrue(check_permutation("aaa", "aaa"))
        self.assertTrue(check_permutation("aaab", "baaa"))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            check_permutation(1, 2)
        with self.assertRaises(TypeError):
            check_permutation("abc", 123)
