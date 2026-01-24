import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_typical_case(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 9)

    def test_edge_case(self):
        grid = [[1, 2], [3, 4]]
        n = 2
        self.assertEqual(max_sum_rectangular_grid(grid, n), 4)

    def test_edge_case2(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 1
        self.assertEqual(max_sum_rectangular_grid(grid, n), 1)

    def test_edge_case3(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 0
        with self.assertRaises(IndexError):
            max_sum_rectangular_grid(grid, n)

    def test_invalid_input(self):
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 'a'
        with self.assertRaises(TypeError):
            max_sum_rectangular_grid(grid, n)
