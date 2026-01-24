import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_input(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

    def test_edge_case2(self):
        tri = [[1, 2, 3], [4, 5]]
        self.assertEqual(max_path_sum(tri, 2, 3), 5)

    def test_edge_case3(self):
        tri = [[1, 2, 3]]
        self.assertEqual(max_path_sum(tri, 1, 3), 1)

    def test_edge_case4(self):
        tri = [[1, 2]]
        self.assertEqual(max_path_sum(tri, 1, 2), 2)

    def test_edge_case5(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_invalid_input1(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 3, 4)

    def test_invalid_input2(self):
        tri = [[1, 2, 3]]
        with self.assertRaises(TypeError):
            max_path_sum(123, 3, 3)

    def test_invalid_input3(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(TypeError):
            max_path_sum(tri, '3', 3)

    def test_invalid_input4(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            max_path_sum(tri, 3, '3')

    def test_invalid_input5(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            max_path_sum('123', 3, 3)
