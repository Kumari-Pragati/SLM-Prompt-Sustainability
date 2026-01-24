import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (3, 4))

    def test_edge_case(self):
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -2))

    def test_boundary_case(self):
        self.assertEqual(max_Product([0, 1, 2, 3]), (1, 2))

    def test_single_element(self):
        self.assertEqual(max_Product([1]), "No pairs exists")

    def test_empty_list(self):
        self.assertEqual(max_Product([]), "No pairs exists")

    def test_negative_and_positive_numbers(self):
        self.assertEqual(max_Product([-1, 1, -2, 2]), (-1, 1))

    def test_duplicate_numbers(self):
        self.assertEqual(max_Product([1, 2, 2, 3]), (2, 2))
