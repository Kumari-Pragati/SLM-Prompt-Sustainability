import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_max_product(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 60)
        self.assertEqual(max_product([1, 0, 3, 4, 5], 5), 0)
        self.assertEqual(max_product([1, -2, -3, 4, 5], 5), 60)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_product([-1, -2, 3, 4, 5], 5), 60)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 900)
