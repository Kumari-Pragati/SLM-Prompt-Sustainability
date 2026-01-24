import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_max_similar_indices(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])
        self.assertEqual(max_similar_indices([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4), (7, 8)]), [(1, 2), (3, 4), (5, 6)])
        self.assertEqual(max_similar_indices([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4), (5, 7)]), [(1, 2), (3, 4), (5, 7)])
        self.assertEqual(max_similar_indices([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4), (5, 6), (7, 8)]), [(1, 2), (3, 4), (5, 6)])

    def test_max_similar_indices_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_max_similar_indices_single_element_lists(self):
        self.assertEqual(max_similar_indices([(1, 2)], [(1, 2)]), [(1, 2)])
        self.assertEqual(max_similar_indices([(1, 2)], [(1, 3)]), [(1, 2)])
        self.assertEqual(max_similar_indices([(1, 2)], [(3, 2)]), [(1, 2)])

    def test_max_similar_indices_lists_of_different_lengths(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4)])
        self.assertEqual(max_similar_indices([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4)]), [(1, 2), (3, 4)])
