import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_simple_permutation(self):
        self.assertTrue(check_permutation("abc", "bca"))
        self.assertTrue(check_permutation("a", "a"))
        self.assertTrue(check_permutation("aaa", "aaa"))

    def test_edge_cases(self):
        self.assertFalse(check_permutation("abc", "abd"))
        self.assertFalse(check_permutation("", ""))
        self.assertFalse(check_permutation("a", ""))
        self.assertFalse(check_permutation("", "a"))

    def test_complex_permutation(self):
        self.assertTrue(check_permutation("tactcoa", "tacotoca"))
        self.assertFalse(check_permutation("tactcoa", "tacotocb"))
        self.assertTrue(check_permutation("0123456789", "9876543210"))
        self.assertFalse(check_permutation("0123456789", "01234567890"))
