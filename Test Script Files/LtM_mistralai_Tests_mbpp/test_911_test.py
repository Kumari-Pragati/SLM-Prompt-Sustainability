import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)
        self.assertEqual(maximum_product([-1, -2, -3]), 6)
        self.assertEqual(maximum_product([1, 2, -3]), 6)
        self.assertEqual(maximum_product([3, 2, 1]), 6)

    def test_edge_cases(self):
        self.assertEqual(maximum_product([1, 2]), 2)
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -24)
        self.assertEqual(maximum_product([0, 0, 0]), 0)
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1]), 1)

    def test_complex(self):
        self.assertEqual(maximum_product([1, -1, 1, -1]), 1)
        self.assertEqual(maximum_product([1, 2, -2, 3]), 6)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -120)
        self.assertEqual(maximum_product([100, 200, 300, 400, 500]), 120000)
