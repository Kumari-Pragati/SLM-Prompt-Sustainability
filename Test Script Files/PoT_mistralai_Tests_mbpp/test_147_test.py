import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_path_sum([[3, 8, 8, 5], [2, 2, 4, 9], [7, 5, 8, 4], [6, 7, 9, 2]], 4, 4), 33)
        self.assertEqual(max_path_sum([[1], [2]], 1, 1), 2)
        self.assertEqual(max_path_sum([[1, 1, 1, 1], [1, 1, 1, 1]], 2, 2), 3)

    def test_edge_case(self):
        self.assertEqual(max_path_sum([[1]], 1, 1), 1)
        self.assertEqual(max_path_sum([[1, 2], [3, 4]], 2, 2), 7)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 24)

    def test_corner_case(self):
        self.assertEqual(max_path_sum([[0], [0]], 1, 1), 0)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 0]], 3, 3), 21)
        self.assertEqual(max_path_sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 3, 3), -20)
