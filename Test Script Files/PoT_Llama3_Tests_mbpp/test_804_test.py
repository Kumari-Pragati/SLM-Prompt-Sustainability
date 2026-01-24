import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_edge_case_zero(self):
        self.assertTrue(is_Product_Even([0, 0, 0], 3))

    def test_edge_case_one(self):
        self.assertFalse(is_Product_Even([1, 1, 1], 3))

    def test_edge_case_all_even(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))

    def test_edge_case_all_odd(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_edge_case_mixed(self):
        self.assertFalse(is_Product_Even([1, 2, 3], 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            is_Product_Even('abc', 3)

    def test_invalid_input_length(self):
        with self.assertRaises(TypeError):
            is_Product_Even([1, 2], 3)
