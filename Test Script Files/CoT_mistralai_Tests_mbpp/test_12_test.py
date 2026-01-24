import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_sort_matrix_empty_list(self):
        self.assertEqual(sort_matrix([]), [])

    def test_sort_matrix_single_element(self):
        self.assertEqual(sort_matrix([[1]]), [[1]])

    def test_sort_matrix_single_row_multiple_elements(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_sort_matrix_multiple_rows_multiple_elements(self):
        self.assertEqual(sort_matrix([[3, 2], [1, 4], [5, 7]]), [[1, 2], [3, 4], [5, 7]])

    def test_sort_matrix_matrix_with_duplicates(self):
        self.assertEqual(sort_matrix([[1, 2], [1, 3], [2, 4]]), [[1, 2], [1, 3], [2, 4]])

    def test_sort_matrix_matrix_with_negative_numbers(self):
        self.assertEqual(sort_matrix([[-1, 2], [3, -4], [-5, 7]]), [[-5, -1], [-4, 3], [2, 7]])

    def test_sort_matrix_matrix_with_mixed_numbers(self):
        self.assertEqual(sort_matrix([[1, -2], [3, 4], [-5, 7]]), [[-5, -2], [1, 2], [3, 4]])

    def test_sort_matrix_matrix_with_only_negative_numbers(self):
        self.assertEqual(sort_matrix([[-1, -2], [-3, -4], [-5, -7]]), [[-7, -5], [-4, -3], [-2, -1]])
