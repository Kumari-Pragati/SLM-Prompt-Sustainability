import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]),
                         [(5, 6), (7, 8)])

    # Test for edge and boundary conditions
    def test_empty_inputs(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_minimum_values(self):
        self.assertEqual(max_similar_indices([(0, 0), (0, 0)], [(0, 0), (0, 0)]),
                         [(0, 0), (0, 0)])

    def test_maximum_values(self):
        self.assertEqual(max_similar_indices([(1000, 1000), (1000, 1000)],
                                             [(1000, 1000), (1000, 1000)]),
                         [(1000, 1000), (1000, 1000)])

    # Test for more complex or corner cases
    def test_mixed_inputs(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 3), (7, 2)]),
                         [(5, 3), (7, 4)])

    def test_negative_inputs(self):
        self.assertEqual(max_similar_indices([(-1, -2), (-3, -4)],
                                             [(-5, -6), (-7, -8)]),
                         [(-1, -2), (-3, -4)])
