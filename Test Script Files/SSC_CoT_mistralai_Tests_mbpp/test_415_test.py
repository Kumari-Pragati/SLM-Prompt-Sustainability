import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (1, 5))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5]), (-1, -5))
        self.assertEqual(max_Product([0, 2, 3, 4, 5]), (0, 5))

    def test_edge_cases(self):
        self.assertEqual(max_Product([]), ("No pairs exists"))
        self.assertEqual(max_Product([1]), ("No pairs exists"))
        self.assertEqual(max_Product([1, 1]), (1, 1))

    def test_negative_numbers(self):
        self.assertEqual(max_Product([-1, 1]), (-1, 1))
        self.assertEqual(max_Product([-1, -2, 1]), (-1, -2))

    def test_invalid_input(self):
        self.assertEqual(max_Product("abc"), ("No pairs exists"))
        self.assertEqual(max_Product([1, "a"]), ("No pairs exists"))
        self.assertEqual(max_Product([1, None]), ("No pairs exists"))
