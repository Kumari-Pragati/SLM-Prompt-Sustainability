import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_simple_positive_case(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5), 3))

    def test_simple_negative_case(self):
        self.assertFalse(check_K((1, 2, 3, 4, 5), 6))

    def test_empty_tuple(self):
        self.assertFalse(check_K((), 1))

    def test_tuple_with_single_element(self):
        self.assertFalse(check_K((1,), 2))
        self.assertTrue(check_K((1,), 1))

    def test_large_number(self):
        self.assertTrue(check_K((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10))
        self.assertFalse(check_K((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 11))

    def test_negative_numbers(self):
        self.assertTrue(check_K((-1, -2, -3, -4, -5), -3))
        self.assertFalse(check_K((-1, -2, -3, -4, -5), -6))

    def test_mixed_numbers(self):
        self.assertTrue(check_K((1, -2, 3, -4, 5), 3))
        self.assertFalse(check_K((1, -2, 3, -4, 5), 6))
