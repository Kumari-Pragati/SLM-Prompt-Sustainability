import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_max_product(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 60)
        self.assertEqual(max_product([5, 2, 3, 4, 1], 5), 20)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6], 6), 120)
        self.assertEqual(max_product([6, 5, 4, 3, 2, 1], 6), 30)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7], 7), 210)
        self.assertEqual(max_product([7, 6, 5, 4, 3, 2, 1], 7), 42)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7, 8], 8), 336)
        self.assertEqual(max_product([8, 7, 6, 5, 4, 3, 2, 1], 8), 56)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 540)
        self.assertEqual(max_product([9, 8, 7, 6, 5, 4, 3, 2, 1], 9), 72)

    def test_max_product_edge_cases(self):
        self.assertEqual(max_product([1], 1), 1)
        self.assertEqual(max_product([1, 2], 2), 2)
        self.assertEqual(max_product([1, 2, 3], 3), 6)
        self.assertEqual(max_product([1, 2, 3, 4], 4), 12)
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 15)
