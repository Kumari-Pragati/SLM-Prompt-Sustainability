import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(min_product_tuple([(1, 1), (2, 2), (3, 3)]), 1)

    def test_simple_negative(self):
        self.assertEqual(min_product_tuple([(-1, -1), (-2, -2), (-3, -3)]), 1)

    def test_mixed_positive_negative(self):
        self.assertEqual(min_product_tuple([(1, -1), (-2, 2), (3, -3)]), 6)

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)

    def test_single_item(self):
        self.assertEqual(min_product_tuple([(1, 1)]), 1)

    def test_minimum_values(self):
        self.assertEqual(min_product_tuple([(1, 1), (1, -1), (-1, 1), (-1, -1)]), 1)

    def test_maximum_values(self):
        self.assertEqual(min_product_tuple([(sys.maxsize, sys.maxsize), (-sys.maxsize, -sys.maxsize)]), sys.maxsize)
