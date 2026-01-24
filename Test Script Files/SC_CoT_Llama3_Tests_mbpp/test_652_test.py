import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(matrix_to_list(test_list), '[(1, 4, 7), (2, 5, 8), (3, 6, 9)]')

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(matrix_to_list(test_list), '[]')

    def test_edge_case_single_element_list(self):
        test_list = [[1, 2, 3]]
        self.assertEqual(matrix_to_list(test_list), '[(1, 2, 3)]')

    def test_edge_case_single_element_sublist(self):
        test_list = [[1], [2], [3]]
        self.assertEqual(matrix_to_list(test_list), '[(1,), (2,), (3,)]')

    def test_edge_case_single_element_sublist_with_duplicates(self):
        test_list = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(matrix_to_list(test_list), '[(1, 1, 3), (2, 2, 3)]')

    def test_invalid_input_non_list(self):
        test_list = 'not a list'
        with self.assertRaises(TypeError):
            matrix_to_list(test_list)

    def test_invalid_input_sublist_with_non_int_elements(self):
        test_list = [[1, 'a', 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            matrix_to_list(test_list)
