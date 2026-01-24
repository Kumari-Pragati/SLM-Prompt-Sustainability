import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_input(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case(self):
        A = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case2(self):
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case3(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(min_sum_path(A), 1)

    def test_invalid_input(self):
        A = 'invalid input'
        with self.assertRaises(TypeError):
            min_sum_path(A)

    def test_empty_input(self):
        A = []
        with self.assertRaises(IndexError):
            min_sum_path(A)

    def test_single_element_input(self):
        A = [[1]]
        with self.assertRaises(IndexError):
            min_sum_path(A)
