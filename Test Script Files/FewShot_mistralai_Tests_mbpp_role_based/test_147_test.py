import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):
    def test_valid_input(self):
        tri = [[6, 1, 8],
               [2, 7, 3],
               [4, 5, 9]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 23)

    def test_empty_triangle(self):
        tri = []
        self.assertEqual(max_path_sum(tri, 0, 0), 0)

    def test_single_row(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_single_column(self):
        tri = [[1], [2], [3]]
        self.assertEqual(max_path_sum(tri, 3, 1), 7)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            max_path_sum(tri, -1, 1)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            max_path_sum(tri, 0, 0)
