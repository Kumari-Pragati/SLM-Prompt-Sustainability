import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6]]), '[(1, 4), (2, 5), (3, 6)]')

    def test_edge_case_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_edge_case_single_element_list(self):
        self.assertEqual(matrix_to_list([[1]]), '[(1,)]')

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4]]), '[(1, 4), (2, 4), (3, 4)]')

    def test_edge_case_single_element_sublist_with_empty_sublist(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], []]), '[]')

    def test_edge_case_single_element_sublist_with_empty_sublist_and_single_element(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4]]), '[(1, 4), (2, 4), (3, 4)]')

    def test_edge_case_single_element_sublist_with_empty_sublist_and_single_element_with_empty_sublist(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], []]), '[]')

    def test_edge_case_single_element_sublist_with_empty_sublist_and_single_element_with_empty_sublist_and_single_element(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4]]), '[(1, 4), (2, 4), (3, 4)]')
