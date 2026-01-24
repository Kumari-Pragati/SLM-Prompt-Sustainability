import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([10, 20, 30, 40, 50], 5), 12000000)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Product([1], 1), 1)
        self.assertEqual(find_Product([], 0), 1)
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), -120)
        self.assertEqual(find_Product([0, 2, 3, 4, 5], 5), 0)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(find_Product([1, 2, 2, 3, 3], 5), 12)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 3628800)
