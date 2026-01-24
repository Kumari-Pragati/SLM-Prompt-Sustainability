import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)
        self.assertEqual(get_median([1, 3, 5], [], 3), 3)
        self.assertEqual(get_median([], [2, 4, 6], 3), 4)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 1), 3)
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 0), None)

    def test_edge_and_boundary(self):
        self.assertEqual(get_median([-1000000, -1, 0, 1, 1000000], [-1000001, -1, 0, 1, 1000001], 5), 0)
        self.assertEqual(get_median([], [], 0), None)
        self.assertEqual(get_median([1], [], 1), 1)
        self.assertEqual(get_median([], [1], 1), 1)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 6), (2 + 3) / 2)
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 7), (2 + 3) / 2)
