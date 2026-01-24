import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_max_Product(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (5, 4))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5]), (-1, -2))
        self.assertEqual(max_Product([1, -2, 3, -4, 5]), (5, -4))
        self.assertEqual(max_Product([1]), "No pairs exists")
        self.assertEqual(max_Product([]), "No pairs exists")
