import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_normal_input(self):
        tri = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(max_sum(tri, 3), 0)

        tri = [[3, 2, 1], [8, 5, 3], [4, 9, 7]]
        self.assertEqual(max_sum(tri, 3), 12)

    def test_edge_input(self):
        tri = [[0], [1]]
        self.assertEqual(max_sum(tri, 2), 1)

        tri = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.assertEqual(max_sum(tri, 5), 0)

        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(max_sum(tri, 4), 12)

    def test_corner_input(self):
        tri = [[1], [2], [3], [4], [5]]
        self.assertEqual(max_sum(tri, 5), 5)

        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        self.assertEqual(max_sum(tri, 6), 23)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_sum(None, 3)

        with self.assertRaises(ValueError):
            max_sum(tri, -1)
