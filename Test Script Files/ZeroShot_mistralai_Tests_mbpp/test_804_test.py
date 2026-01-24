import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_odd_length_list(self):
        self.assertFalse(is_Product_Even([1, 2, 3], 3))
        self.assertFalse(is_Product_Even([3, 2, 1], 3))

    def test_even_length_list_with_even_elements(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([6, 4, 2], 3))

    def test_even_length_list_with_odd_elements(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))
        self.assertFalse(is_Product_Even([5, 3, 1], 3))

    def test_single_element(self):
        self.assertFalse(is_Product_Even([1], 1))
        self.assertTrue(is_Product_Even([2], 1))
