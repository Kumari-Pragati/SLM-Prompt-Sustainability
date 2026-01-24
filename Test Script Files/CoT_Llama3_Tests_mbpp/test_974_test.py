import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_min_sum_path_typical(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_min_sum_path_edge(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_min_sum_path_invalid_input(self):
        A = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            min_sum_path(A)

    def test_min_sum_path_empty_input(self):
        A = []
        with self.assertRaises(IndexError):
            min_sum_path(A)

    def test_min_sum_path_single_element_input(self):
        A = [[1]]
        self.assertEqual(min_sum_path(A), 1)

    def test_min_sum_path_single_element_input_empty(self):
        A = [[]]
        with self.assertRaises(IndexError):
            min_sum_path(A)
