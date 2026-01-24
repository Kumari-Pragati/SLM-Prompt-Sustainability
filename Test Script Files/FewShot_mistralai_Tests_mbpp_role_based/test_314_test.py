import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):
    def test_typical_use_case(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 13)
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 28)

    def test_edge_case_small_grid(self):
        grid = [[1], [2]]
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 3)

    def test_edge_case_single_row(self):
        grid = [[1, 2, 3], [4], [5, 6, 7]]
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 10)
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 19)

    def test_edge_case_single_column(self):
        grid = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 10)
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 15)

    def test_boundary_case_empty_grid(self):
        grid = []
        self.assertEqual(max_sum_rectangular_grid(grid, 1), 0)

    def test_boundary_case_single_element(self):
        grid = [[1]]
        self.assertEqual(max_sum_rectangular_grid(grid, 1), 1)
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 1)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid(grid, -1)
