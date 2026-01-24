import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        n = 4
        self.assertEqual(max_sum(tri, n), 23)

    def test_edge_case_n_equals_1(self):
        tri = [[3]]
        n = 1
        self.assertEqual(max_sum(tri, n), 3)

    def test_boundary_case_n_equals_2(self):
        tri = [[3], [7, 4]]
        n = 2
        self.assertEqual(max_sum(tri, n), 10)

    def test_corner_case_all_elements_are_zero(self):
        tri = [[0], [0, 0], [0, 0, 0]]
        n = 3
        self.assertEqual(max_sum(tri, n), 0)

    def test_corner_case_negative_numbers(self):
        tri = [[-3], [-7, -4], [-2, -4, -6], [-8, -5, -9, -3]]
        n = 4
        self.assertEqual(max_sum(tri, n), -3)

    def test_corner_case_single_row(self):
        tri = [[10]]
        n = 1
        self.assertEqual(max_sum(tri, n), 10)
