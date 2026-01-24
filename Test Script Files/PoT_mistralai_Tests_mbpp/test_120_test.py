import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product_tuple([1, 2, 3, -4, 5]), 60)
        self.assertEqual(max_product_tuple([-1, -2, -3, 4, -5]), 60)
        self.assertEqual(max_product_tuple([0, 0, 0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product_tuple([1]), 1)
        self.assertEqual(max_product_tuple([-1]), 1)
        self.assertEqual(max_product_tuple([0]), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_product_tuple([-1, -2, -3]), 6)
        self.assertEqual(max_product_tuple([-1, -2, 3]), 6)
        self.assertEqual(max_product_tuple([-1, 2, -3]), 6)
