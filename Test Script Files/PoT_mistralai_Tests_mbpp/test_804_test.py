import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([1, 3, 5], 3))
        self.assertTrue(is_Product_Even([2, 4, 6, 8], 4))
        self.assertTrue(is_Product_Even([], 0))
        self.assertTrue(is_Product_Even([1], 1))

    def test_edge_case(self):
        self.assertFalse(is_Product_Even([0], 1))
        self.assertFalse(is_Product_Even([1, 2, 3], 0))
        self.assertFalse(is_Product_Even([2, 4, 6, 8, 10], 5))
        self.assertFalse(is_Product_Even([-1, -3, -5], 3))
