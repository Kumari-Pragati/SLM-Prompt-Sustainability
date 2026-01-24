import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_maximum_product(self):
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -6)
        self.assertEqual(maximum_product([-1, -2, -3, 4]), 24)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -6)
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 120)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6]), -6)
        self.assertEqual(maximum_product([0, 0, 0, 0, 0]), 0)
        self.assertEqual(maximum_product([1, 1, 1, 1, 1]), 1)
        self.assertEqual(maximum_product([-1, -1, -1, -1, -1]), -1)
