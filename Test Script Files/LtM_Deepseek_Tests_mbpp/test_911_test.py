import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)
        self.assertEqual(maximum_product([-1, -2, -3]), -6)
        self.assertEqual(maximum_product([1, 1, 1]), 1)

    def test_edge_conditions(self):
        self.assertEqual(maximum_product([0, 0, 0]), 0)
        self.assertEqual(maximum_product([1, 2]), 2)
        self.assertEqual(maximum_product([-1, -2]), -2)
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([]), None)

    def test_complex_cases(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -6)
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product([-1, -2, 3, 4]), 24)
        self.assertEqual(maximum_product([-1, 2, -3, 4]), 24)
        self.assertEqual(maximum_product([-1, -2, -3, 4]), 12)
