import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_permutation("abc", "cab"))

    def test_simple_invalid(self):
        self.assertFalse(check_permutation("abc", "def"))

    def test_empty_strings(self):
        self.assertFalse(check_permutation("", ""))
        self.assertFalse(check_permutation("", "abc"))
        self.assertFalse(check_permutation("abc", ""))

    def test_single_character(self):
        self.assertTrue(check_permutation("a", "a"))
        self.assertFalse(check_permutation("a", "b"))

    def test_same_string(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_reverse_string(self):
        self.assertTrue(check_permutation("abc", "cba"))

    def test_long_strings(self):
        self.assertTrue(check_permutation("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))

    def test_long_strings_with_spaces(self):
        self.assertTrue(check_permutation("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba "))
