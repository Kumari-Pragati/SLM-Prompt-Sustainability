import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (5, 6)]), 6)

    def test_edge_case_zero(self):
        self.assertEqual(min_product_tuple([(0, 0), (1, 2), (3, 4)]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(min_product_tuple([(-1, 2), (3, 4), (-5, 6)]), 6)

    def test_edge_case_positive(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (5, 6)]), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(min_product_tuple([(1, 2)]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(min_product_tuple([]), None)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_product_tuple("Invalid input")

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            min_product_tuple([1, 2, 3])

    def test_invalid_input_non_int(self):
        with self.assertRaises(TypeError):
            min_product_tuple([(1, 'a'), (3, 4)])
