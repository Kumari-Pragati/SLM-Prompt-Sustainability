import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_typical_use_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case_empty_array(self):
        A = []
        with self.assertRaises(IndexError):
            min_sum_path(A)

    def test_edge_case_single_element_array(self):
        A = [[1]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case_single_row_array(self):
        A = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case_single_column_array(self):
        A = [[1], [2], [3]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case_zero_element_array(self):
        A = [[0]]
        self.assertEqual(min_sum_path(A), 0)

    def test_edge_case_negative_elements_array(self):
        A = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(min_sum_path(A), -1)
