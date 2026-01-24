import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_permutation("abc", "bca"))
        self.assertTrue(check_permutation("123", "321"))
        self.assertTrue(check_permutation("hello", "ollhe"))

    def test_empty_strings(self):
        self.assertTrue(check_permutation("", ""))

    def test_single_character_strings(self):
        self.assertTrue(check_permutation("a", "a"))

    def test_identical_strings(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_different_lengths(self):
        self.assertFalse(check_permutation("abc", "abcd"))
        self.assertFalse(check_permutation("abcd", "abc"))

    def test_case_sensitivity(self):
        self.assertFalse(check_permutation("Abc", "abc"))

    def test_whitespace_sensitivity(self):
        self.assertFalse(check_permutation("abc def", "def abc"))

    def test_special_characters(self):
        self.assertTrue(check_permutation("abc!@#", "@#!cba"))
