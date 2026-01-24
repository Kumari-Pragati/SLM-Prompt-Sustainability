import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_permutation('abc', 'bca'))
        self.assertTrue(check_permutation('123', '321'))
        self.assertFalse(check_permutation('abc', 'def'))

    def test_edge_cases(self):
        self.assertTrue(check_permutation('', ''))
        self.assertFalse(check_permutation('a', ''))
        self.assertFalse(check_permutation('', 'a'))

    def test_boundary_conditions(self):
        self.assertTrue(check_permutation('a'*10000, 'a'*10000[::-1]))
        self.assertFalse(check_permutation('a'*10000, 'b'*10000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_permutation(123, 'abc')
        with self.assertRaises(TypeError):
            check_permutation('abc', 123)
