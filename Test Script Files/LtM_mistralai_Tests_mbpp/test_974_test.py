import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(min_sum_path([[1], [5, 3], [4, 8, 2]]), 1)
        self.assertEqual(min_sum_path([[1], [1, 1], [1, 1, 1]])), 1)

    def test_edge_input(self):
        self.assertEqual(min_sum_path([[]]), 0)
        self.assertEqual(min_sum_path([[1]]), 1)
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 1)
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1)

    def test_boundary_input(self):
        self.assertEqual(min_sum_path([[-1], [-2, -3], [-4, -5, -6]]), -1)
        self.assertEqual(min_sum_path([[1000000000], [1000000001, 1000000002], [1000000003, 1000000004, 1000000005]])), 1000000001)
