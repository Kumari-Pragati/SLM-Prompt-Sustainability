import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_permutation('abc', 'bca'))
        self.assertTrue(check_permutation('123', '321'))
        self.assertTrue(check_permutation('hello', 'ollhe'))

    def test_edge_cases(self):
        self.assertTrue(check_permutation('', ''))
        self.assertFalse(check_permutation('a', ''))
        self.assertFalse(check_permutation('', 'a'))

    def test_special_cases(self):
        self.assertTrue(check_permutation('aabb', 'abab'))
        self.assertFalse(check_permutation('abc', 'abcd'))
        self.assertFalse(check_permutation('abc', 'def'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_permutation(123, 'abc')
        with self.assertRaises(TypeError):
            check_permutation('abc', 123)
