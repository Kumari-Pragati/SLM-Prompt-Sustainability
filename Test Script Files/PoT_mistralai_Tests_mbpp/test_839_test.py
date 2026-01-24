import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_tuple_typical_case(self):
        self.assertEqual(sort_tuple([(1, 2), (3, 4), (2, 1)]), [(1, 2), (2, 1), (3, 4)])
        self.assertEqual(sort_tuple([(5, 6), (3, 4), (2, 1)]), [(2, 1), (3, 4), (5, 6)])
        self.assertEqual(sort_tuple([(1, 2), (1, 3), (1, 4)]), [(1, 2), (1, 3), (1, 4)])

    def test_sort_tuple_edge_case_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_sort_tuple_edge_case_single_item(self):
        self.assertEqual(sort_tuple([(1, 2)]), [(1, 2)])

    def test_sort_tuple_edge_case_duplicate_first_elements(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 3), (1, 2)]), [(1, 2), (1, 2), (1, 3)])

    def test_sort_tuple_edge_case_duplicate_tuples(self):
        self.assertEqual(sort_tuple([(1, 2), (1, 2)]), [(1, 2), (1, 2)])

    def test_sort_tuple_corner_case_first_element_zero(self):
        self.assertEqual(sort_tuple([(0, 2), (3, 4), (2, 1)]), [(0, 2), (2, 1), (3, 4)])

    def test_sort_tuple_corner_case_negative_first_element(self):
        self.assertEqual(sort_tuple([(-1, 2), (3, 4), (2, 1)]), [(-1, 2), (2, 1), (3, 4)])
