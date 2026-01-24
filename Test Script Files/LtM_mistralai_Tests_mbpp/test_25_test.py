import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([2, 2, 2, 2, 2], 5), 2**5)
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case(self):
        self.assertEqual(find_Product([], 0), 1)
        self.assertEqual(find_Product([0], 1), 0)
        self.assertEqual(find_Product([1, 1, 1, 1, 1, 1], 6), 1)
        self.assertEqual(find_Product([1000000000, 1000000000], 2), 1000000000**2)

    def test_complex_case(self):
        self.assertEqual(find_Product([1, 2, 1, 2, 1, 2], 6), 2)
        self.assertEqual(find_Product([-1, -2, -1, -2, -1, -2], 6), 2)
        self.assertEqual(find_Product([0, 0, 1, 0, 1, 0], 6), 0)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6], 6), 720)
