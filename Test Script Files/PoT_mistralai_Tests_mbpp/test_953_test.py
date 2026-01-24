import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 4], 3), 2)
        self.assertEqual(subset([1, 1, 1, 1, 2], 4), 1)
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(subset([], 0), 0)
        self.assertEqual(subset([1], 1), 1)
        self.assertEqual(subset([1, 1], 2), 1)
        self.assertEqual(subset([1, 1, 1], 3), 1)

    def test_corner_cases(self):
        self.assertEqual(subset([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(subset([1, 1, 1, 1, 2], 0), 0)
        self.assertEqual(subset([1, 1, 1, 1, 2], 6), 0)
