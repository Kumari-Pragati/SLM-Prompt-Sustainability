import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Product_Even([2, 3, 4], 3))

    def test_edge_case(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_boundary_case(self):
        self.assertFalse(is_Product_Even([], 0))
        self.assertFalse(is_Product_Even([1], 1))

    def test_special_case(self):
        self.assertTrue(is_Product_Even([0], 1))
        self.assertFalse(is_Product_Even([2, 3, 5], 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Product_Even("not a list", 1)
        with self.assertRaises(TypeError):
            is_Product_Even([1, 2, 3], "not an integer")
