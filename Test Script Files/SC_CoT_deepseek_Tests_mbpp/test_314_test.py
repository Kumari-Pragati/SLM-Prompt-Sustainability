import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):
    
    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

    def test_edge_case_n_equals_0(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 0
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)

    def test_edge_case_single_row_grid(self):
        grid = [[1, 2, 3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_edge_case_single_column_grid(self):
        grid = [[1], [2], [3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_corner_case_all_elements_are_positive(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

    def test_corner_case_all_elements_are_negative(self):
        grid = [[-1, -2, -3], [-4, -5, -6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -1)

    def test_invalid_input_grid_not_list(self):
        grid = "not a list"
        n = 3
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)

    def test_invalid_input_grid_elements_not_list(self):
        grid = [[1, 2, 3], "not a list"]
        n = 3
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)

    def test_invalid_input_n_not_integer(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = "not an integer"
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)
