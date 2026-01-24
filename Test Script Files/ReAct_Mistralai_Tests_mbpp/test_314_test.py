import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(max_sum_rectangular_grid([], 2), 0)

    def test_single_row_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 2), 3)
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 1), 2)

    def test_single_column_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 2), 3)
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 1), 2)

    def test_square_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 2), 10)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 1), 7)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 3), 10)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 4), 10)

    def test_rectangular_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 2), 19)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 1), 15)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 3), 27)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_rectangular_grid([[-1, 2], [3, -4]], 2), 1)

    def test_zero_numbers(self):
        self.assertEqual(max_sum_rectangular_grid([[0, 0], [0, 0]], 2), 0)

    def test_large_numbers(self):
        self.assertEqual(max_sum_rectangular_grid([[1000000001, 2], [3, 4000000004]], 2), 1000000005)
