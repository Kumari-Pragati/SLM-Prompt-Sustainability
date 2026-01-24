import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        A = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
        self.assertEqual(min_sum_path(A), 20)

    def test_single_row(self):
        A = [[1, 2, 3, 4, 5]]
        self.assertEqual(min_sum_path(A), 15)

    def test_single_column(self):
        A = [[1], [2], [3], [4], [5]]
        self.assertEqual(min_sum_path(A), 15)

    def test_empty_list(self):
        A = []
        self.assertIsNone(min_sum_path(A))

    def test_negative_numbers(self):
        A = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(min_sum_path(A), -24)

    def test_zeroes(self):
        A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(min_sum_path(A), 0)

    def test_large_numbers(self):
        A = [[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]]
        self.assertEqual(min_sum_path(A), 30000)
