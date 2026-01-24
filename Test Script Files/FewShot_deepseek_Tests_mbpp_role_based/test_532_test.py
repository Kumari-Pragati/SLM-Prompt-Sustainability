import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_permutation('abc', 'bca'))

    def test_empty_strings(self):
        self.assertTrue(check_permutation('', ''))

    def test_different_lengths(self):
        self.assertFalse(check_permutation('abc', 'abcd'))

    def test_same_length_different_strings(self):
        self.assertFalse(check_permutation('abc', 'def'))

    def test_case_sensitivity(self):
        self.assertFalse(check_permutation('abc', 'ABC'))

    def test_whitespace_handling(self):
        self.assertTrue(check_permutation('a b c', 'b c a'))

    def test_numeric_strings(self):
        self.assertTrue(check_permutation('123', '321'))

    def test_special_characters(self):
        self.assertTrue(check_permutation('abc!@#', '!@#abc'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_permutation(123, 'abc')
