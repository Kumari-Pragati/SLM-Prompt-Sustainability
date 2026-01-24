import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_sort_matrix_empty_list(self):
        self.assertEqual(sort_matrix([]), [])

    def test_sort_matrix_single_element(self):
        self.assertEqual(sort_matrix([[1]]), [[1]])

    def test_sort_matrix_single_row_multiple_columns(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_sort_matrix_multiple_rows_single_column(self):
        self.assertEqual(sort_matrix([[1], [2], [3]]), [ [1], [2], [3] ])

    def test_sort_matrix_multiple_rows_multiple_columns(self):
        self.assertEqual(sort_matrix([[3, 2], [1, 5], [4, 7]]), [[1, 2], [3, 5], [4, 7]])

    def test_sort_matrix_reverse_order(self):
        self.assertEqual(sort_matrix([[7, 2], [1, 5], [4, 3]]), [[1, 2], [4, 3], [7, 5]])

    def test_sort_matrix_negative_numbers(self):
        self.assertEqual(sort_matrix([[-3, 2], [-1, 5], [-4, -7]]), [[-4, -7], [-3, -2], [-1, 5]])

    def test_sort_matrix_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_matrix([[1, 'a'], [2, 3]])
