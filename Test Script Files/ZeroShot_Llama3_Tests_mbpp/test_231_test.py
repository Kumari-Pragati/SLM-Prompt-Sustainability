import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_max_sum(self):
        tri = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(max_sum(tri, 3), 7)

        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        self.assertEqual(max_sum(tri, 4), 10)

        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15]]
        self.assertEqual(max_sum(tri, 4), 15)

        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
        self.assertEqual(max_sum(tri, 5), 20)

    def test_max_sum_edge_cases(self):
        tri = [[1]]
        self.assertEqual(max_sum(tri, 1), 1)

        tri = [[1, 2]]
        self.assertEqual(max_sum(tri, 2), 2)

        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_sum(tri, 2), 4)
