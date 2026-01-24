import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):
    
    def test_typical_case(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 23)

    def test_edge_case(self):
        tri = [[3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 3)

    def test_corner_case(self):
        tri = [[3], [7, 0], [2, 0, 6], [8, 0, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        self.assertEqual(max_path_sum(tri, m, n), 23)

    def test_invalid_input(self):
        tri = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        m = len(tri)
        n = len(tri[0])
        with self.assertRaises(TypeError):
            max_path_sum(tri, m)
        with self.assertRaises(TypeError):
            max_path_sum(tri, m, n, 1)
        with self.assertRaises(ValueError):
            max_path_sum([], 0, 0)
        with self.assertRaises(ValueError):
            max_path_sum([[3]], 1, 0)
