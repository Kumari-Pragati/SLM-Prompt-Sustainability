import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

    def test_single_row(self):
        grid = [[1, 2, 3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_single_column(self):
        grid = [[1], [2], [3]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

    def test_negative_numbers(self):
        grid = [[-1, -2, -3], [-4, -5, -6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -1)

    def test_empty_grid(self):
        grid = []
        n = 0
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)

    def test_invalid_input(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 'invalid'
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)
