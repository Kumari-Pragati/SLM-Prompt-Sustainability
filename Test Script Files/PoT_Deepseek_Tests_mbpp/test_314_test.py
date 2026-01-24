import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 21)

    def test_edge_case_single_row(self):
        grid = [[1, 2, 3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_edge_case_single_column(self):
        grid = [[1], [2], [3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_boundary_case_empty_grid(self):
        grid = []
        n = 0
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)

    def test_corner_case_negative_numbers(self):
        grid = [[-1, -2, -3], [-4, -5, -6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -1)

    def test_corner_case_large_numbers(self):
        grid = [[1000, 2000, 3000], [4000, 5000, 6000]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 21000)
