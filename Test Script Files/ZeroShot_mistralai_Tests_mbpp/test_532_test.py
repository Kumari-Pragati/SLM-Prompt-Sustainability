import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_same_permutation(self):
        self.assertTrue(check_permutation("abc", "cab"))
        self.assertTrue(check_permutation("aabbcc", "bcaaaccc"))
        self.assertTrue(check_permutation("12345", "54321"))

    def test_not_same_permutation(self):
        self.assertFalse(check_permutation("abc", "abd"))
        self.assertFalse(check_permutation("aabbcc", "bcaaddc"))
        self.assertFalse(check_permutation("12345", "12346"))
