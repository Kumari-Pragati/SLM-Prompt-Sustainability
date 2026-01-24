import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(check_permutation("abc", "bca"))
        self.assertTrue(check_permutation("ABC", "CAB"))

    def test_edge_cases(self):
        self.assertTrue(check_permutation("a", "a"))
        self.assertTrue(check_permutation("aa", "aa"))
        self.assertTrue(check_permutation("abcd", "dcba"))
        self.assertTrue(check_permutation("ABCD", "DCBA"))
        self.assertTrue(check_permutation("123", "321"))
        self.assertTrue(check_permutation("123", "312"))

    def test_boundary_cases(self):
        self.assertFalse(check_permutation("a", "b"))
        self.assertFalse(check_permutation("ab", "ba"))
        self.assertFalse(check_permutation("abc", "abd"))
        self.assertFalse(check_permutation("ABC", "ABD"))
        self.assertFalse(check_permutation("12", "21"))
        self.assertFalse(check_permutation("12", "13"))

    def test_invalid_inputs(self):
        self.assertFalse(check_permutation(None, "abc"))
        self.assertFalse(check_permutation("abc", None))
        self.assertFalse(check_permutation("", "abc"))
        self.assertFalse(check_permutation("abc", ""))
        self.assertFalse(check_permutation("abc", 1))
        self.assertFalse(check_permutation(1, "abc"))
