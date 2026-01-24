import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Product_Even([2, 3, 4], 3))

    def test_edge_case_empty_array(self):
        self.assertFalse(is_Product_Even([], 0))

    def test_boundary_case_single_even_number(self):
        self.assertTrue(is_Product_Even([2], 1))

    def test_boundary_case_single_odd_number(self):
        self.assertFalse(is_Product_Even([3], 1))

    def test_corner_case_all_even_numbers(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_corner_case_all_odd_numbers(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_corner_case_mixed_numbers(self):
        self.assertTrue(is_Product_Even([1, 2, 3, 4, 5], 5))
