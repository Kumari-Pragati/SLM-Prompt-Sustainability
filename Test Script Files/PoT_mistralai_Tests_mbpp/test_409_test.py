import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (-5, 6)]), 12)
        self.assertEqual(min_product_tuple([(0, 0), (1, 1), (-1, -1)]), 0)
        self.assertEqual(min_product_tuple([(10, 2), (-5, 6), (0, 0)]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)

    def test_edge_case_single_item(self):
        self.assertEqual(min_product_tuple([(1,)]), 0)
        self.assertEqual(min_product_tuple([(-1,)]), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4), (-5, -6)]), 30)
