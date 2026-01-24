import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(max_similar_indices([(0, 0)], [(1, 1)]), [(0, 0)])
        self.assertEqual(max_similar_indices([(1, 1)], [(0, 0)]), [(0, 0)])

    def test_equal_lists(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1), (2, 2)],
                                              [(0, 0), (1, 1), (2, 2)])
                         , [(2, 2), (1, 1), (0, 0)])

    def test_different_lengths(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1)], [(0, 0), (1, 1), (2, 2)])
                         , [(1, 1)])

    def test_different_elements(self):
        self.assertEqual(max_similar_indices([(0, 0), (1, 1), (2, 2)],
                                              [(3, 3), (4, 4), (5, 5)])
                         , [])
