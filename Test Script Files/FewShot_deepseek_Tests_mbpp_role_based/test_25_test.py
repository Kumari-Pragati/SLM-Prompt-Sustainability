import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 720)

    def test_edge_condition(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 1)

    def test_boundary_condition(self):
        arr = [0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(find_Product(arr, n), 0)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4]
        n = -1
        with self.assertRaises(IndexError):
            find_Product(arr, n)
