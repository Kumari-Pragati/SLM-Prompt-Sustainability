import unittest
from mbpp_804_code import is_Product_Even

class TestIsProductEven(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [2, 3, 4, 5]
        n = len(arr)
        self.assertTrue(is_Product_Even(arr, n))

    def test_edge_condition(self):
        arr = [1, 3, 5, 7]
        n = len(arr)
        self.assertFalse(is_Product_Even(arr, n))

    def test_boundary_condition(self):
        arr = [2]
        n = len(arr)
        self.assertTrue(is_Product_Even(arr, n))

    def test_invalid_input(self):
        arr = [2, 3, 4, 5]
        n = -1
        with self.assertRaises(Exception):
            is_Product_Even(arr, n)
