import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_even_product(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([4, 2, 6], 3))
        self.assertTrue(is_Product_Even([6, 4, 2], 3))

    def test_odd_product(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))
        self.assertFalse(is_Product_Even([5, 1, 3], 3))
        self.assertFalse(is_Product_Even([3, 5, 1], 3))

    def test_empty_list(self):
        self.assertFalse(is_Product_Even([], 3))

    def test_single_element(self):
        self.assertFalse(is_Product_Even([1], 1))
        self.assertFalse(is_Product_Even([2], 1))
        self.assertFalse(is_Product_Even([3], 1))

    def test_zero_length_array(self):
        self.assertFalse(is_Product_Even([0], 0))
