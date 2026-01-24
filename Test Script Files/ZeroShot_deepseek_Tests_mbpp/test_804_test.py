import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_all_even(self):
        self.assertTrue(is_Product_Even([2, 4, 6, 8], 4))

    def test_all_odd(self):
        self.assertFalse(is_Product_Even([1, 3, 5, 7], 4))

    def test_mixed(self):
        self.assertTrue(is_Product_Even([1, 2, 3, 4], 4))

    def test_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_single_element(self):
        self.assertFalse(is_Product_Even([3], 1))
        self.assertTrue(is_Product_Even([2], 1))
