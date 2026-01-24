import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):
    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_sum_rectangular_grid(grid, 3), 21)

    def test_edge_case_small_grid(self):
        grid = [[1], [2]]
        self.assertEqual(max_sum_rectangular_grid(grid, 2), 3)

    def test_edge_case_large_grid(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(max_sum_rectangular_grid(grid, 4), 63)

    def test_edge_case_small_n(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_sum_rectangular_grid(grid, 1), 10)

    def test_edge_case_large_n(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_sum_rectangular_grid(grid, 5), 10)

    def test_invalid_input_empty_grid(self):
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid([], 3)

    def test_invalid_input_non_list_grid(self):
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid('not a list', 3)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid([[1, 2], [3, 4]], -1)
