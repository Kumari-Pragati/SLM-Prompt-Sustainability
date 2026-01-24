import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_max_path_sum(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 15)

        tri = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_path_sum(tri, 2, 3), 6)

        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

        tri = [[1, 2]]
        self.assertEqual(max_path_sum(tri, 1, 2), 2)

        tri = [[1, 2, 3, 4, 5]]
        self.assertEqual(max_path_sum(tri, 5, 5), 9)

        tri = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 9, 9), 15)
