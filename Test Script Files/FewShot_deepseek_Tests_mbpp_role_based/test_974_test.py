import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_typical_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 13)

    def test_single_row(self):
        A = [[1, 2, 3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_single_column(self):
        A = [[1], [2], [3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_empty_matrix(self):
        A = []
        self.assertIsNone(min_sum_path(A))

    def test_negative_numbers(self):
        A = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(min_sum_path(A), -13)

    def test_zeroes(self):
        A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(min_sum_path(A), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_sum_path("not a matrix")
