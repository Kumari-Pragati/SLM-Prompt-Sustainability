import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):
    def test_typical_use_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 9)

    def test_edge_case(self):
        grid = [[1, 2], [3, 4]]
        n = 2
        self.assertEqual(max_sum_rectangular_grid(grid, n), 4)

    def test_boundary_case(self):
        grid = [[1, 2, 3, 4], [5, 6, 7, 8]]
        n = 4
        self.assertEqual(max_sum_rectangular_grid(grid, n), 8)

    def test_invalid_input(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 'a'
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)
