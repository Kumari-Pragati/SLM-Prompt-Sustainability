import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_max_sum_rectangular_grid(self):
        # Test case 1: Normal case
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

        # Test case 2: All elements are positive
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 2
        self.assertEqual(max_sum_rectangular_grid(grid, n), 9)

        # Test case 3: All elements are negative
        grid = [[-1, -2, -3], [-4, -5, -6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), -1)

        # Test case 4: One row is all zeros
        grid = [[0, 0, 0], [4, 5, 6]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 15)

        # Test case 5: One column is all zeros
        grid = [[1, 2, 0], [4, 5, 0]]
        n = 3
        self.assertEqual(max_sum_rectangular_grid(grid, n), 11)

        # Test case 6: n is 1
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 1
        self.assertEqual(max_sum_rectangular_grid(grid, n), 6)

        # Test case 7: n is 0
        grid = [[1, 2, 3], [4, 5, 6]]
        n = 0
        self.assertEqual(max_sum_rectangular_grid(grid, n), 0)
