import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):
    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

    def test_edge_case(self):
        grid = [[1], [2]]
        n = 1
        self.assertEqual(max_sum_rectangular_grid(grid, n), 2)

    def test_boundary_case(self):
        grid = [[0, 0], [0, 0]]
        n = 2
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)

    def test_invalid_input(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = -1
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid(grid, n)
