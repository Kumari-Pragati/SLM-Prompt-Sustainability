import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_simple_permutation(self):
        self.assertTrue(check_permutation('abc', 'bca'))

    def test_empty_strings(self):
        self.assertTrue(check_permutation('', ''))

    def test_same_string(self):
        self.assertTrue(check_permutation('abc', 'abc'))

    def test_different_lengths(self):
        self.assertFalse(check_permutation('abc', 'abcd'))

    def test_case_sensitivity(self):
        self.assertFalse(check_permutation('abc', 'Abc'))

    def test_whitespace_sensitivity(self):
        self.assertFalse(check_permutation('abc ', 'abc'))

    def test_complex_permutation(self):
        self.assertTrue(check_permutation('aabbcc', 'bbaacc'))
