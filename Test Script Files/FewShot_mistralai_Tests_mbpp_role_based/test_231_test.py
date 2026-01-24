import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_typical_use_case(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum(tri, len(tri)), 15)

    def test_edge_case_empty_triangle(self):
        tri = []
        with self.assertRaises(ValueError):
            max_sum(tri, len(tri))

    def test_edge_case_single_row(self):
        tri = [[1]]
        self.assertEqual(max_sum(tri, len(tri)), 1)

    def test_edge_case_single_column(self):
        tri = [[1], [2]]
        self.assertEqual(max_sum(tri, len(tri)), 2)

    def test_boundary_case_one_element(self):
        tri = [[1]]
        self.assertEqual(max_sum(tri, 2), 1)

    def test_boundary_case_two_elements(self):
        tri = [[1], [2]]
        self.assertEqual(max_sum(tri, 3), 2)
