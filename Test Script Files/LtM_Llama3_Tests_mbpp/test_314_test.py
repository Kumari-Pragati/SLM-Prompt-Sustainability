import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_simple_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 9)

    def test_edge_case_empty_grid(self):
        grid = []
        n = 0
        with self.assertRaises(IndexError):
            max_sum_rectangular_grid(grid, n)

    def test_edge_case_single_row(self):
        grid = [[1, 2, 3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_edge_case_single_col(self):
        grid = [[1], [2], [3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_edge_case_max_value(self):
        grid = [[100, 100, 100], [100, 100, 100]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 300)

    def test_edge_case_min_value(self):
        grid = [[-100, -100, -100], [-100, -100, -100]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -300)

    def test_edge_case_negative_values(self):
        grid = [[-1, -2, -3], [-4, -5, -6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -9)

    def test_edge_case_positive_values(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 9)

    def test_edge_case_zero_values(self):
        grid = [[0, 0, 0], [0, 0, 0]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)
