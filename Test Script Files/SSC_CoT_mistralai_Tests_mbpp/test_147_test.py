import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_normal_input(self):
        tri = [[3, 8, 8, 5],
               [2, 2, 5, 1],
               [4, 9, 2, 7],
               [3, 5, 9, 3]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 33)

    def test_edge_input(self):
        tri = [[1], [1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 1)
        tri = [[1, 1], [1, 1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 2)
        tri = [[1, 1, 1], [1, 1, 1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 3)

    def test_boundary_input(self):
        tri = [[1], [2], [3]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 7)
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 10)
        tri = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 20)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            max_path_sum([[1]], 0, 0)
        with self.assertRaises(IndexError):
            max_path_sum([[1]], 1, 0)
        with self.assertRaises(IndexError):
            max_path_sum([[1]], 1, 1)
        with self.assertRaises(IndexError):
            max_path_sum([[1, 2], [3]], 1, 0)
        with self.assertRaises(IndexError):
            max_path_sum([[1, 2], [3]], 1, 2)
