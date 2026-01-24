import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):

    def test_is_Product_Even(self):
        self.assertTrue(is_Product_Even([2, 4, 6], 3))
        self.assertTrue(is_Product_Even([1, 3, 5], 3))
        self.assertFalse(is_Product_Even([2, 4, 6, 7], 4))
        self.assertFalse(is_Product_Even([1, 3, 5, 6], 4))
        self.assertTrue(is_Product_Even([2, 4, 6, 8], 4))
        self.assertTrue(is_Product_Even([1, 3, 5, 7], 4))
        self.assertFalse(is_Product_Even([2, 4, 6, 8, 9], 5))
        self.assertFalse(is_Product_Even([1, 3, 5, 7, 9], 5))
        self.assertTrue(is_Product_Even([2, 4, 6, 8, 10], 5))
        self.assertTrue(is_Product_Even([1, 3, 5, 7, 11], 5))
