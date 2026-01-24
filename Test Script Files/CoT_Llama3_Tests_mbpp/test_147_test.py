import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

    def test_edge_case2(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_invalid_input(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 2, 4)

    def test_invalid_input2(self):
        tri = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 1, 3)
