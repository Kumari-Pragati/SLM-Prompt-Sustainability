import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_simple_input(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 23)

    def test_edge_condition_empty_input(self):
        tri = []
        m = 0
        n = 0
        self.assertEqual(max_path_sum(tri, m, n), 0)

    def test_boundary_condition_minimum_value(self):
        tri = [[-1000]]
        m = 1
        n = 1
        self.assertEqual(max_path_sum(tri, m, n), -1000)

    def test_boundary_condition_maximum_value(self):
        tri = [[2000]]
        m = 1
        n = 1
        self.assertEqual(max_path_sum(max_path_sum, m, n), 2000)

    def test_complex_input(self):
        tri = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 26)
