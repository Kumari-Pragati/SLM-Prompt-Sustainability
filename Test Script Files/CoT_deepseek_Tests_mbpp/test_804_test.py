import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Product_Even([2, 3, 5], 3))

    def test_all_odd_numbers(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_negative_numbers(self):
        self.assertTrue(is_Product_Even([-2, -3, -5], 3))

    def test_zero(self):
        self.assertTrue(is_Product_Even([0], 1))

    def test_large_numbers(self):
        self.assertTrue(is_Product_Even([10**18, 10**18], 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Product_Even("not an array", 1)
