import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_empty_grid(self):
        grid = []
        self.assertEqual(max_sum_rectangular_grid(grid, 1), 0)

    def test_single_row_grid(self):
        grid = [[1], [2], [3]]
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 6)

    def test_single_column_grid(self):
        grid = [[1], [2], [3]]
        self.assertEqual(max_sum_rectangular_grid(grid, 1), 3)

    def test_square_grid(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 36)

    def test_rectangular_grid(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(max_sum_rectangular_grid(grid, 4), 50)

    def test_rectangular_grid_with_zero(self):
        grid = [[0, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(max_sum_rectangular_grid(grid, 4), 49)
