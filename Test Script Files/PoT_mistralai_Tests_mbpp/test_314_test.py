import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 2), 13)
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 1), 2)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 35)

    def test_edge_case_small_grid(self):
        self.assertEqual(max_sum_rectangular_grid([[1]], 1), 1)
        self.assertEqual(max_sum_rectangular_grid([[1, 2]], 1), 2)
        self.assertEqual(max_sum_rectangular_grid([[1, 2]], 2), 3)

    def test_edge_case_large_n(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 4), 13)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 5), 17)

    def test_corner_case_empty_grid(self):
        self.assertEqual(max_sum_rectangular_grid([], 1), 0)

    def test_corner_case_single_row(self):
        self.assertEqual(max_sum_rectangular_grid([[1]], 2), 1)

    def test_corner_case_single_column(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 1), 7)
