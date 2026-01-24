import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (-1, -2)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4)]), 4)

    def test_positive_numbers(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4)]), 2)

    def test_zero_in_list(self):
        self.assertEqual(min_product_tuple([(0, 1), (-1, -2)]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            min_product_tuple([])

    def test_single_tuple(self):
        self.assertEqual(min_product_tuple([(1, 2)]), 2)

    def test_tuple_with_zero(self):
        self.assertEqual(min_product_tuple([(0, 1), (2, 3)]), 0)

    def test_tuple_with_negative_product(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4)]), 4)
