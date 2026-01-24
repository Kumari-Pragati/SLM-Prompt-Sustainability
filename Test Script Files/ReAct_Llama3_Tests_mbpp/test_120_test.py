import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 20)

    def test_edge_case_zero(self):
        self.assertEqual(max_product_tuple([(0, 1), (2, 3)]), 6)

    def test_edge_case_negative(self):
        self.assertEqual(max_product_tuple([(-1, 2), (3, -4)]), 12)

    def test_edge_case_zero_product(self):
        self.assertEqual(max_product_tuple([(0, 0), (2, 3)]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product_tuple([(1,)]), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(TypeError):
            max_product_tuple([])

    def test_edge_case_single_element_zero(self):
        self.assertEqual(max_product_tuple([(0,)]), 0)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(max_product_tuple([(-1,)]), 1)
