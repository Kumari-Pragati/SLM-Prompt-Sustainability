import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_typical_even_product(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_typical_odd_product(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_edge_case_single_element(self):
        self.assertTrue(is_Product_Even([2], 1))

    def test_edge_case_zero_elements(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_edge_case_single_zero(self):
        self.assertTrue(is_Product_Even([0], 1))

    def test_edge_case_all_zeros(self):
        self.assertTrue(is_Product_Even([0, 0, 0], 3))

    def test_edge_case_negative_numbers(self):
        self.assertTrue(is_Product_Even([-2, 2, 4], 3))

    def test_edge_case_mixed_signs(self):
        self.assertTrue(is_Product_Even([-2, 2, 4], 3))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            is_Product_Even([2, 4, 6], 'a')

    def test_invalid_input_non_positive_integer(self):
        with self.assertRaises(TypeError):
            is_Product_Even([2, 4, 6], 0)
