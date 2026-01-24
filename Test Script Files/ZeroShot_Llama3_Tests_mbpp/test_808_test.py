import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_check_k_true(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_check_k_false(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_check_k_empty_tuple(self):
        self.assertFalse(check_K((), 5))

    def test_check_k_single_element(self):
        self.assertTrue(check_K((5,), 5))

    def test_check_k_multiple_occurrences(self):
        self.assertTrue(check_K((1, 2, 2, 3, 3, 3), 3))

    def test_check_k_non_integer(self):
        self.assertFalse(check_K(("a", "b", "c"), "a"))
