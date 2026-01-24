import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):
    def test_typical_case(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 15)

    def test_edge_case1(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

    def test_edge_case2(self):
        tri = [[1], [2]]
        self.assertEqual(max_path_sum(tri, 2, 1), 2)

    def test_edge_case3(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_error_case1(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 2, 3)

    def test_error_case2(self):
        tri = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 1, 4)
