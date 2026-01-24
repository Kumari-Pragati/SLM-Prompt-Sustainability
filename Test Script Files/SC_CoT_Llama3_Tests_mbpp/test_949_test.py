import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sort_list([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_edge_case_single_element_list(self):
        self.assertEqual(sort_list([(1, 2, 3)]), '[(1, 2, 3)]')

    def test_edge_case_sorted_list(self):
        self.assertEqual(sort_list([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')

    def test_edge_case_reverse_sorted_list(self):
        self.assertEqual(sort_list([(7, 8, 9), (4, 5, 6), (1, 2, 3)]), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')

    def test_edge_case_duplicates(self):
        self.assertEqual(sort_list([(1, 2, 3), (4, 4, 5), (7, 8, 9)]), '[(1, 2, 3), (4, 4, 5), (7, 8, 9)]')

    def test_edge_case_empty_tuple(self):
        self.assertEqual(sort_list(()), '[]')

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(sort_list((1, 2, 3)), '[(1, 2, 3)]')

    def test_edge_case_sorted_tuple(self):
        self.assertEqual(sort_list((1, 2, 3), (4, 5, 6), (7, 8, 9)), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')

    def test_edge_case_reverse_sorted_tuple(self):
        self.assertEqual(sort_list((7, 8, 9), (4, 5, 6), (1, 2, 3)), '[(1, 2, 3), (4, 5, 6), (7, 8, 9)]')

    def test_edge_case_duplicates_tuple(self):
        self.assertEqual(sort_list((1, 2, 3), (4, 4, 5), (7, 8, 9)), '[(1, 2, 3), (4, 4, 5), (7, 8, 9)]')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_list('abc')

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            sort_list([1, 2, 3])
