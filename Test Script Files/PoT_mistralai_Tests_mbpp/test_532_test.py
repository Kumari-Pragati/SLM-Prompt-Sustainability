import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_typical_permutation(self):
        self.assertTrue(check_permutation("abc", "bca"))
        self.assertTrue(check_permutation("aabbcc", "abcbac"))

    def test_edge_cases(self):
        self.assertFalse(check_permutation("abc", "abcd"))
        self.assertFalse(check_permutation("", ""))
        self.assertFalse(check_permutation("a", "b"))
        self.assertFalse(check_permutation("aa", "ab"))

    def test_corner_cases(self):
        self.assertTrue(check_permutation("AaBb", "BbAa"))
        self.assertTrue(check_permutation("123", "321"))
        self.assertFalse(check_permutation("123", "1234"))
        self.assertTrue(check_permutation("", " "))
