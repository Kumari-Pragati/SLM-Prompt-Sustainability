import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 120)
        self.assertEqual(max_product_tuple([(2, 3), (4, 5), (6, 7)]), 240)

    def test_negative_numbers(self):
        self.assertEqual(max_product_tuple([(-1, -2), (-3, -4), (-5, -6)]), 120)
        self.assertEqual(max_product_tuple([(-2, -3), (-4, -5), (-6, -7)]), 240)

    def test_zero(self):
        self.assertEqual(max_product_tuple([(0, 0), (1, 2), (3, 4)]), 0)
        self.assertEqual(max_product_tuple([(0, 0), (-1, -2), (-3, -4)]), 0)

    def test_one_element(self):
        self.assertEqual(max_product_tuple([(1,)]), 1)
        self.assertEqual(max_product_tuple([(-1,)]), 1)

    def test_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)
