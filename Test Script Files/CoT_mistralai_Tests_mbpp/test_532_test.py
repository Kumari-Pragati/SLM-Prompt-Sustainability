import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(check_permutation("abc", "bca"))
        self.assertTrue(check_permutation("aabb", "baab"))
        self.assertFalse(check_permutation("abc", "abd"))
        self.assertFalse(check_permutation("abc", "acb"))
        self.assertFalse(check_permutation("", ""))
        self.assertFalse(check_permutation("a", "b"))
        self.assertFalse(check_permutation(None, "abc"))
        self.assertFalse(check_permutation("abc", None))
