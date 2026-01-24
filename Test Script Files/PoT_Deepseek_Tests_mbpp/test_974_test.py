import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_typical_case(self):
        A = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        self.assertEqual(min_sum_path(A), 7)

    def test_edge_case(self):
        A = [[1]]
        self.assertEqual(min_sum_path(A), 1)

    def test_boundary_case(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(min_sum_path(A), 7)

    def test_corner_case(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(min_sum_path(A), 16)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_sum_path("invalid input")
