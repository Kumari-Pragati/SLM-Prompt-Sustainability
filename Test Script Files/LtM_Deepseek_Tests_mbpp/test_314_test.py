import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 2), 6)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 1), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 0), 0)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 3), 7)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 4), 8)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 5), 9)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 2), 6)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 3), 7)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 4), 8)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 5), 9)
