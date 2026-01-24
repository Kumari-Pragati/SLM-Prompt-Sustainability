import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(subset([1, 1, 1, 2], 3), 1)
        self.assertEqual(subset([1, 2, 2, 3], 4), 2)
        self.assertEqual(subset([1, 1, 2, 3], 3), 1)

    def test_edge_cases(self):
        self.assertEqual(subset([], 0), 0)
        self.assertEqual(subset([1], 1), 1)
        self.assertEqual(subset([1, 1], 2), 2)
        self.assertEqual(subset([1, 1, 1], 3), 1)
        self.assertEqual(subset([1, 2, 2, 2], 4), 3)

    def test_boundary_conditions(self):
        self.assertEqual(subset([1, 1, 1, 1], 4), 1)
        self.assertEqual(subset([1, 2, 2, 2, 2], 5), 4)
        self.assertEqual(subset([1, 2, 2, 2, 3], 5), 2)
