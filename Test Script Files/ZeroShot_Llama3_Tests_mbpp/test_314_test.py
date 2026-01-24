import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_max_sum_rectangular_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 3), 9)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3, 4], [5, 6, 7, 8]], 4), 14)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 5, ), 15)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], 6), 18)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], 7), 20)

    def test_max_sum_rectangular_grid_edge_cases(self):
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 1), 1)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3]], 2), 3)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4]], 3), 4)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3, 4], [5]], 4, ), 5)
