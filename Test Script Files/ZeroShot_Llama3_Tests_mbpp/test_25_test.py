import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_find_product(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 5, ), 1)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6], 6), 720)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6, 7], 7, ), 5040)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6, 7, 8], 8, ), 40320)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, ), 362880)

    def test_find_product_edge_cases(self):
        self.assertEqual(find_Product([1], 1), 1)
        self.assertEqual(find_Product([1, 2], 2, ), 2)
        self.assertEqual(find_Product([1, 2, 3], 3, ), 6)
        self.assertEqual(find_Product([1, 2, 3, 4], 4, ), 24)
        self.assertEqual(find_Product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, ), 3628800)
