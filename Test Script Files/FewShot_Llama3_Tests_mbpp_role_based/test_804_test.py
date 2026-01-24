import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_even_product(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_odd_product(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_single_even(self):
        self.assertTrue(is_Product_Even([2], 1))

    def test_single_odd(self):
        self.assertFalse(is_Product_Even([1], 1))

    def test_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_zero_length_array(self):
        self.assertFalse(is_Product_Even([1, 2, 3], 0))
