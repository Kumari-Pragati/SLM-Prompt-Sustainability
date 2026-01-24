import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_same_pair([1, 2, 2], [1, 2, 2]), 2)
        self.assertEqual(count_same_pair([1, 1, 2], [1, 1, 2]), 2)

    def test_edge_cases(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([1], []), 0)
        self.assertEqual(count_same_pair([], [1]), 0)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_boundary_cases(self):
        self.assertEqual(count_same_pair([0, 0, 0], [0, 0, 0]), 3)
        self.assertEqual(count_same_pair([-1, -1, 1], [-1, -1, 1]), 2)
        self.assertEqual(count_same_pair([1.0, 1.0, 2.0], [1.0, 1.0, 2.0]), 2)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_same_pair, [1, 2], 3)
        self.assertRaises(TypeError, count_same_pair, (1, 2), [3])
