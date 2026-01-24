import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):
    def test_similar_indices_positive(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]), [(3, 4), (7, 8)])

    def test_similar_indices_zero(self):
        self.assertEqual(max_similar_indices([(0, 0), (0, 0)], [(0, 0), (0, 0)]), [(0, 0), (0, 0)])

    def test_similar_indices_negative(self):
        self.assertEqual(max_similar_indices([(-1, -2), (-3, -4)], [(-5, -6), (-7, -8)]), [(-3, -4), (-7, -8)])

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            max_similar_indices([(1, 2), (3, 4)], [(5, 6)])

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            max_similar_indices([], [])
