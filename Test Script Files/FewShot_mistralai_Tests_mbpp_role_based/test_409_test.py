import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (5, 6)]), 6)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4), (-5, -6)]), 36)

    def test_zero(self):
        self.assertEqual(min_product_tuple([(0, 0), (1, 2), (0, 3)]), 0)

    def test_one_element(self):
        self.assertEqual(min_product_tuple([(1,)]), 0)

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)
