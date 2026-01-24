import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(check_permutation("abc", "cab"))

    def test_non_permutation(self):
        self.assertFalse(check_permutation("abc", "def"))

    def test_same_string(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_empty_string(self):
        self.assertTrue(check_permutation("", ""))

    def test_empty_string_with_non_empty_string(self):
        self.assertFalse(check_permutation("", "abc"))

    def test_non_empty_string_with_empty_string(self):
        self.assertFalse(check_permutation("abc", ""))
