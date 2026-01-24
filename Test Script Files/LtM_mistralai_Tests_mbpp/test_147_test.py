import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_path_sum([[1], [2]], 2, 1), 3)
        self.assertEqual(max_path_sum([[1, 3], [2, 5]], 2, 2), 7)

    def test_edge_and_boundary(self):
        self.assertEqual(max_path_sum([[0], [0]], 2, 1), 0)
        self.assertEqual(max_path_sum([[1000000000], [1000000000]], 2, 1), 1000000000)
        self.assertEqual(max_path_sum([[1], [2], [3]], 3, 3), 6)
        self.assertEqual(max_path_sum([[1], [2]], 1, 1), 2)
        self.assertEqual(max_path_sum([[1], [2], [3], [4]], 4, 4), 10)
        self.assertEqual(max_path_sum([[1], [2], [3], [4]], 1, 1), 1)

    def test_complex(self):
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3), 20)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1), 1)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 4), 30)
        self.assertEqual(max_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2), 15)
