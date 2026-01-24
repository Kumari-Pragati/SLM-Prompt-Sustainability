import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 20)

    def test_edge_case_negative(self):
        self.assertEqual(max_product_tuple([(-1, 2), (3, 4)]), 20)

    def test_edge_case_positive(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 20)

    def test_edge_case_zero(self):
        self.assertEqual(max_product_tuple([(0, 0), (0, 0)]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product_tuple([(1, 1)]), 1)

    def test_edge_case_empty(self):
        self.assertEqual(max_product_tuple([]), None)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(max_product_tuple([(0, 0)]), 0)

    def test_edge_case_single_element_nonzero(self):
        self.assertEqual(max_product_tuple([(1, 1)]), 1)
