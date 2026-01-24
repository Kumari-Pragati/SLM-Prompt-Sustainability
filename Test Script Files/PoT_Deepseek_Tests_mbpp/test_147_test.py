import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 23)

    def test_edge_case(self):
        tri = [[1]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 1)

    def test_boundary_case(self):
        tri = [[3], [7, 4]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 13)

    def test_invalid_input(self):
        tri = []
        m = 0
        n = 0
        with self.assertRaises(Exception):
            max_path_sum(tri, m, n)
