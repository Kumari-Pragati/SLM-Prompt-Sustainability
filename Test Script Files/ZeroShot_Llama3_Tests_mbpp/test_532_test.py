import unittest
from mbpp_532_code import check_permutation

class TestCheckPermutation(unittest.TestCase):

    def test_true_permutation(self):
        self.assertTrue(check_permutation("abc", "cab"))

    def test_false_permutation(self):
        self.assertFalse(check_permutation("abc", "def"))

    def test_same_string(self):
        self.assertTrue(check_permutation("abc", "abc"))

    def test_empty_string(self):
        self.assertTrue(check_permutation("", ""))

    def test_empty_string2(self):
        self.assertFalse(check_permutation("abc", ""))

    def test_empty_string3(self):
        self.assertFalse(check_permutation("", "abc"))

    def test_permutation_with_spaces(self):
        self.assertTrue(check_permutation("a b c", "c b a"))

    def test_permutation_with_spaces2(self):
        self.assertFalse(check_permutation("a b c", "d e f"))
