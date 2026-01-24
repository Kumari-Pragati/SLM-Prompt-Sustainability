import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(largest_pos([1, 2, 3]), 3)
        self.assertEqual(largest_pos([-1, -2, -3]), -1)
        self.assertEqual(largest_pos([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(largest_pos([1000000000000000000]), 1000000000000000000)
        self.assertEqual(largest_pos([-1000000000000000000]), -1000000000000000000)
        self.assertEqual(largest_pos([]), None)
        self.assertEqual(largest_pos([float('inf'), 1, float('-inf')]), float('inf'))
        self.assertEqual(largest_pos([float('-inf'), -1, float('inf')]), float('-inf'))
