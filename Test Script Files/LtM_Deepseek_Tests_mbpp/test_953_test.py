import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(subset([1, 2, 2, 3], 4), 2)
        self.assertEqual(subset([1, 1, 1, 1], 4), 4)
        self.assertEqual(subset([1, 2, 3, 4], 4), 1)

    def test_edge_conditions(self):
        self.assertEqual(subset([], 0), 0)
        self.assertEqual(subset([1], 1), 1)
        self.assertEqual(subset([1, 1, 1, 1, 1], 5), 5)

    def test_boundary_conditions(self):
        self.assertEqual(subset([1, 2, 2, 3], 4), 2)
        self.assertEqual(subset([1, 1, 1, 1, 1, 1], 6), 6)

    def test_complex_cases(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)
        self.assertEqual(subset([1, 2, 2, 2, 3, 3], 6), 3)
        self.assertEqual(subset([1, 2, 2, 2, 2, 2], 6), 6)
