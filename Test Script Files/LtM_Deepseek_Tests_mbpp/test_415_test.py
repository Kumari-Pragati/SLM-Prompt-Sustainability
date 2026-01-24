import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (3, 4))
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (3, 5))

    def test_edge_conditions(self):
        self.assertEqual(max_Product([1]), "No pairs exists")
        self.assertEqual(max_Product([]), "No pairs exists")
        self.assertEqual(max_Product([-1, -2]), (-1, -2))
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_complex_cases(self):
        self.assertEqual(max_Product([-1, -2, 3, 4]), (3, 4))
        self.assertEqual(max_Product([1, -2, -3, 4]), (1, 4))
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))
        self.assertEqual(max_Product([1, 2, 3, 4, 0]), (3, 4))
