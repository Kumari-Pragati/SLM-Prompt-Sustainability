import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(max_product_tuple(list1), 12)

    def test_edge_case_empty_list(self):
        list1 = []
        self.assertEqual(max_product_tuple(list1), 0)

    def test_edge_case_single_element_list(self):
        list1 = [(1, 1)]
        self.assertEqual(max_product_tuple(list1), 1)

    def test_edge_case_negative_numbers(self):
        list1 = [(-1, 2), (3, -4), (5, 6)]
        self.assertEqual(max_product_tuple(list1), 12)

    def test_edge_case_zero(self):
        list1 = [(0, 2), (3, 0), (0, 0)]
        self.assertEqual(max_product_tuple(list1), 0)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_product_tuple("invalid input")
