import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (1, 4))
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -4))
        self.assertEqual(max_Product([0, 0]), (0, 0))
        self.assertEqual(max_Product([1, 0, 3, 4]), (1, 4))
        self.assertEqual(max_Product([-1, 0, -3, -4]), (-1, -4))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_Product([]), ("No pairs exists"))
        self.assertEqual(max_Product([1]), ("No pairs exists"))
        self.assertEqual(max_Product([1, 1]), (1, 1))
        self.assertEqual(max_Product([1, 1, 1]), (1, 1))
        self.assertEqual(max_Product([1, 1, 1, 1]), (1, 1))
