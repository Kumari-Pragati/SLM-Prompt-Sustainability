import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_same_length_permutations(self):
        self.assertTrue(check_permutation('abc', 'bca'))

    def test_different_lengths(self):
        self.assertFalse(check_permutation('abc', 'abcd'))

    def test_same_length_non_permutations(self):
        self.assertFalse(check_permutation('abc', 'def'))

    def test_empty_strings(self):
        self.assertTrue(check_permutation('', ''))

    def test_single_character_strings(self):
        self.assertTrue(check_permutation('a', 'a'))
        self.assertFalse(check_permutation('a', 'b'))
