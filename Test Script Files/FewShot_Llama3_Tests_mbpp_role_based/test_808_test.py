import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):
    def test_true_positive(self):
        self.assertTrue(check_K((1, 2, 3, 4), 4))

    def test_true_negative(self):
        self.assertFalse(check_K((1, 2, 3, 4), 5))

    def test_false_positive(self):
        self.assertFalse(check_K((1, 2, 3, 4), 3))

    def test_false_negative(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))

    def test_single_element_tuple(self):
        self.assertFalse(check_K((1,), 2))

    def test_K_in_tuple(self):
        self.assertTrue(check_K((1, 2, 3, 4), 1))
