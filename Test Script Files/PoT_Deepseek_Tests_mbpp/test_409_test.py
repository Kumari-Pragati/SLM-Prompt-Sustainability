import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2), (-3, 4), (5, -6)]), 6)

    def test_negative_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(-1, -2), (-3, -4), (-5, -6)]), 10)

    def test_positive_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2), (3, 4), (5, 6)]), 6)

    def test_zero_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(0, 2), (3, 4), (5, 6)]), 0)

    def test_single_tuple(self):
        self.assertAlmostEqual(min_product_tuple([(1, 2)]), 2)

    def test_empty_list(self):
        self.assertIsNone(min_product_tuple([]))

    def test_large_numbers(self):
        self.assertAlmostEqual(min_product_tuple([(1000000000, 2000000000), (-3000000000, 4000000000), (-5000000000, 6000000000)]), 2000000000000000)
