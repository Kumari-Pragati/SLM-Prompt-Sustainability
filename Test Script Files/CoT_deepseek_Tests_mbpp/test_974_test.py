import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 16)

    def test_single_row(self):
        A = [[1, 2, 3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_single_column(self):
        A = [[1], [2], [3]]
        self.assertEqual(min_sum_path(A), 6)

    def test_empty_list(self):
        A = []
        self.assertIsNone(min_sum_path(A))

    def test_negative_numbers(self):
        A = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(min_sum_path(A), -16)

    def test_zeroes(self):
        A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(min_sum_path(A), 0)

    def test_large_numbers(self):
        A = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        self.assertEqual(min_sum_path(A), 2400)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_sum_path("not a list")

        with self.assertRaises(ValueError):
            min_sum_path([1, 2, 3])

        with self.assertRaises(TypeError):
            min_sum_path([[1, 2, "3"], [4, 5, 6], [7, 8, 9]])
