import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_typical_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case(self):
        A = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case2(self):
        A = [[1, 2], [3, 4], [5, 6, 7]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case3(self):
        A = [[1, 2, 3], [4, 5], [6, 7, 8]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case4(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(min_sum_path(A), 1)

    def test_edge_case5(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
        self.assertEqual(min_sum_path(A), 1)

    def test_error_case(self):
        A = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            min_sum_path(A)
