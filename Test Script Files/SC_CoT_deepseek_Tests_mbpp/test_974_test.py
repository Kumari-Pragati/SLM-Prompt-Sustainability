import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 16)

    def test_edge_case_single_row(self):
        A = [[1, 2, 3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_edge_case_single_column(self):
        A = [[1], [2], [3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_edge_case_empty(self):
        A = []
        self.assertIsNone(min_sum_path(A))

    def test_corner_case_negative_numbers(self):
        A = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(min_sum_path(A), -30)

    def test_corner_case_zeroes(self):
        A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(min_sum_path(A), 0)

    def test_invalid_input_non_list(self):
        A = 123
        with self.assertRaises(TypeError):
            min_sum_path(A)

    def test_invalid_input_nested_list_with_non_list(self):
        A = [[1, 2, 3], 'a', [4, 5, 6]]
        with self.assertRaises(TypeError):
            min_sum_path(A)

    def test_invalid_input_nested_list_with_different_lengths(self):
        A = [[1, 2, 3], [4, 5], [6]]
        with self.assertRaises(ValueError):
            min_sum_path(A)
