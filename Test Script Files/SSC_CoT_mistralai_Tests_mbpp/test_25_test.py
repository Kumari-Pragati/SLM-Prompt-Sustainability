import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(find_Product([0, 0, 1, 2, 3], 5), 15)

    def test_edge_cases(self):
        self.assertEqual(find_Product([1], 1), 1)
        self.assertEqual(find_Product([1, 1], 2), 1)
        self.assertEqual(find_Product([1, 2, 1], 3), 2)
        self.assertEqual(find_Product([1, 2, 3, 1], 4), 6)
        self.assertEqual(find_Product([1, 2, 3, 4, 1], 5), 24)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 1], 6), 120)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Product(1, 2)
        with self.assertRaises(TypeError):
            find_Product('abc', 1)
        with self.assertRaises(TypeError):
            find_Product([], 1)
