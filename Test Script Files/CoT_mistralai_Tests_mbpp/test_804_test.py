import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_all_even(self):
        self.assertTrue(is_Product_Even([0, 2, 4], 3))

    def test_all_odd(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_mixed_even_odd(self):
        self.assertTrue(is_Product_Even([0, 1, 2, 3, 4], 5))

    def test_single_element(self):
        self.assertFalse(is_Product_Even([1], 1))
        self.assertTrue(is_Product_Even([2], 1))

    def test_negative_numbers(self):
        self.assertTrue(is_Product_Even([-2, -4], 2))

    def test_zero(self):
        self.assertFalse(is_Product_Even([0], 1))

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, is_Product_Even, [1.5, 2], 2)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, is_Product_Even, [1, 2, 3], 'n')
