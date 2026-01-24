import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(min_product_tuple(list1), 2)

    def test_edge_case_zero(self):
        list1 = [(0, 0), (1, 2), (3, 4)]
        self.assertEqual(min_product_tuple(list1), 0)

    def test_edge_case_negative(self):
        list1 = [(1, -2), (3, -4), (5, -6)]
        self.assertEqual(min_product_tuple(list1), 2)

    def test_edge_case_single_element(self):
        list1 = [(1, 2)]
        self.assertEqual(min_product_tuple(list1), 2)

    def test_edge_case_empty_list(self):
        list1 = []
        with self.assertRaises(IndexError):
            min_product_tuple(list1)
