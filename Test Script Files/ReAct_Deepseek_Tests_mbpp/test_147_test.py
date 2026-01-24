import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(triangle)
        n = len(triangle[0])
        self.assertEqual(max_path_sum(triangle, m, n), 23)

    def test_edge_case_single_row(self):
        triangle = [[5]]
        m = len(triangle)
        n = len(triangle[0])
        self.assertEqual(max_path_sum(triangle, m, n), 5)

    def test_edge_case_empty_triangle(self):
        triangle = []
        m = len(triangle)
        n = len(triangle[0]) if triangle else 0
        self.assertEqual(max_path_sum(triangle, m, n), 0)

    def test_error_case_invalid_triangle(self):
        triangle = [[3], [7, 4], [2, 4, 6, 7]]  # Inconsistent row length
        m = len(triangle)
        n = len(triangle[0])
        with self.assertRaises(Exception):
            max_path_sum(triangle, m, n)
