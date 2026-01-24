import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(subset([1, 1, 1, 2, 3], 3), 1)
        self.assertEqual(subset([1, 1, 1, 2, 3], 4), 1)
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(subset([], 0), 0)
        self.assertEqual(subset([1], 1), 1)
        self.assertEqual(subset([1, 1], 2), 2)
        self.assertEqual(subset([1, 1, 1], 3), 1)
        self.assertEqual(subset([1, 1, 1, 1], 4), 1)

    def test_boundary_cases(self):
        self.assertEqual(subset([1, 1, 1, 2, 2], 3), 2)
        self.assertEqual(subset([1, 1, 1, 2, 2, 2], 4), 2)
        self.assertEqual(subset([1, 1, 1, 2, 2, 2, 3], 5), 1)
        self.assertEqual(subset([1, 1, 1, 2, 2, 2, 3, 3], 6), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            subset([], -1)
        with self.assertRaises(ValueError):
            subset([1], -1)
        with self.assertRaises(ValueError):
            subset([1, 1], -1)
        with self.assertRaises(ValueError):
            subset([1, 1, 1], -1)
        with self.assertRaises(ValueError):
            subset([1, 1, 1], n) for n in (-1, float('nan'), float('inf'))
