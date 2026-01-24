import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4)]), 2)

    def test_edge_case_zero(self):
        self.assertEqual(min_product_tuple([(0, 0), (1, 2)]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(min_product_tuple([(-1, 2), (3, 4)]), 2)

    def test_edge_case_positive(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4)]), 2)

    def test_edge_case_zero_list(self):
        self.assertEqual(min_product_tuple([(0, 0)]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(min_product_tuple([(1, 1)]), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(TypeError):
            min_product_tuple([])

    def test_edge_case_non_list_input(self):
        with self.assertRaises(TypeError):
            min_product_tuple("test")
