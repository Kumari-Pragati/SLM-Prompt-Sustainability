import unittest
from mbpp_314_code import max_sum_rectangular_grid

class TestMaxSumRectangularGrid(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 2), 13)
        self.assertEqual(max_sum_rectangular_grid([[1], [2]], 2), 2)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3, 4]], 2), 7)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 31)

    def test_edge_cases(self):
        self.assertEqual(max_sum_rectangular_grid([[1]], 1), 1)
        self.assertEqual(max_sum_rectangular_grid([[1, 2], [3]], 1), 3)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5], [6]], 3), 15)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 0), 0)
        self.assertEqual(max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], 4), 13)

    def test_empty_grid(self):
        self.assertEqual(max_sum_rectangular_grid([], 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid([[1, 2, 3], [4, 5, 6]], -1)
        with self.assertRaises(ValueError):
            max_sum_rectangular_grid([[1, 2, 3]], "not_a_number")
