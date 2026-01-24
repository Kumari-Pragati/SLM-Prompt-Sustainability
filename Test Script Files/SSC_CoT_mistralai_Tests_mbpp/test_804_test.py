import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([1, 3, 5], 3))

    def test_edge_input(self):
        self.assertTrue(is_Product_Even([0], 1))
        self.assertTrue(is_Product_Even([2], 1))
        self.assertFalse(is_Product_Even([1], 1))

    def test_boundary_input(self):
        self.assertTrue(is_Product_Even([0, 1], 2))
        self.assertFalse(is_Product_Even([1, 0], 2))
        self.assertFalse(is_Product_Even([1, 1], 2))

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_Product_Even, [1, 2, 3], 'a')
        self.assertRaises(TypeError, is_Product_Even, [1, 2, 3], -1)
