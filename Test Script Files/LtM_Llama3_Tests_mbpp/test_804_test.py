import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([1, 2, 3], 3))
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_Product_Even([], 0))
        self.assertFalse(is_Product_Even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
        self.assertTrue(is_Product_Even([2], 1))
        self.assertFalse(is_Product_Even([1], 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Product_Even("hello", 3)
        with self.assertRaises(TypeError):
            is_Product_Even([1, 2, 3], "hello")
