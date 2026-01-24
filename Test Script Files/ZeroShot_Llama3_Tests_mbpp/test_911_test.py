import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_maximum_product(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -6)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 60)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6]), -6)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7]), 140)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6, -7]), -42)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8]), 168)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6, -7, -8]), -56)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 216)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -72)
