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

    def test_single_char(self):
        self.assertTrue(check_permutation("a", "a"))

    def test_empty_string_with_non_empty(self):
        self.assertFalse(check_permutation("", "abc"))

    def test_non_empty_string_with_empty(self):
        self.assertFalse(check_permutation("abc", ""))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_permutation(123, "abc")

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            check_permutation("abc", 123)
