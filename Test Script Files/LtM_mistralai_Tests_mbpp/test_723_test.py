import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([4, 4, 4], [4, 4, 4]), 3)
        self.assertEqual(count_same_pair([5, 5, 6], [5, 5, 6]), 2)

    def test_edge_and_boundary(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([0], [0]), 1)
        self.assertEqual(count_same_pair([-10, -10], [10, 10]), 0)
        self.assertEqual(count_same_pair([255, 255, 255], [0, 0, 0]), 0)

    def test_complex(self):
        self.assertEqual(count_same_pair([1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 1, 1]), 4)
        self.assertEqual(count_same_pair([1, 1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 1, 1, 1]), 3)
        self.assertEqual(count_same_pair([1, 1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 1, 1, 2]), 3)
