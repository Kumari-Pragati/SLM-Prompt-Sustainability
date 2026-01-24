import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_simple_even_product(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_simple_odd_product(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_empty_list(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_single_element(self):
        self.assertFalse(is_Product_Even([1], 1))
        self.assertTrue(is_Product_Even([2], 1))

    def test_negative_numbers(self):
        self.assertTrue(is_Product_Even([-2, -4, -6], 3))

    def test_zero(self):
        self.assertFalse(is_Product_Even([0], 1))

    def test_large_numbers(self):
        self.assertTrue(is_Product_Even([2 ** 31 - 1, 2 ** 31 - 1], 2))
