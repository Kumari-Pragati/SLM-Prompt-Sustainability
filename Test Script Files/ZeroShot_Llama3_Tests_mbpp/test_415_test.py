import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_max_product(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (1, 5))
        self.assertEqual(max_Product([-1, 2, 3, 4, 5]), (-1, 5))
        self.assertEqual(max_Product([-1, -2, 3, 4, 5]), (-2, 5))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6]), (1, 6))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6]), (-6, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7]), (1, 7))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7]), (-7, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8]), (1, 8))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8]), (-8, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9]), (1, 9))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9]), (-9, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), (1, 10))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), (-10, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), (1, 11))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), (-11, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), (1, 12))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), (-12, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), (1, 13))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]), (-13, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), (1, 14))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]), (-14, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), (1, 15))
        self.assertEqual(max_Product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]), (-15, -1))
        self.assertEqual(max_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), (1, 16))
        self.assertEqual(max_Product([-1, -2