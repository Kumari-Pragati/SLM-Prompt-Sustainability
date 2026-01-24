import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(is_Product_Even([2, 3, 4], 3))
        self.assertFalse(is_Product_Even([1, 3, 5], 3))

    def test_edge_conditions(self):
        self.assertFalse(is_Product_Even([1, 3, 5], 0))
        self.assertFalse(is_Product_Even([], 0))
        self.assertFalse(is_Product_Even([1], 1))

    def test_complex_cases(self):
        self.assertTrue(is_Product_Even([2, 2, 2], 3))
        self.assertFalse(is_Product_Even([1, 1, 1], 3))
        self.assertTrue(is_Product_Even([2, 3, 4, 5, 6], 5))
        self.assertFalse(is_Product_Even([1, 3, 5, 7, 9], 5))
