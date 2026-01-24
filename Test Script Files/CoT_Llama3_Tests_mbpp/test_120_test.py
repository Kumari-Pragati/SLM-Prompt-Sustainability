import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 12)

    def test_edge_case_negative(self):
        self.assertEqual(max_product_tuple([(-1, 2), (3, -4), (5, 6)]), 12)

    def test_edge_case_zero(self):
        self.assertEqual(max_product_tuple([(0, 2), (3, 0), (5, 6)]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product_tuple([(1,)]), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_product_tuple([]), 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_product_tuple("Invalid input")

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            max_product_tuple([1, 2, 3])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            max_product_tuple([(1, '2'), (3, 4)])
