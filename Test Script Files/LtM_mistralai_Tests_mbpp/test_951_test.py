import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_simple_same_lists(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_simple_different_lists(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]), [(0, 0), (1, 0)])

    def test_empty_lists(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_single_element_lists(self):
        self.assertEqual(max_similar_indices([(1, 2)], [(3, 4)]), [(0, 0)])
        self.assertEqual(max_similar_indices([(3, 4)], [(1, 2)]), [(1, 0)])

    def test_max_values(self):
        self.assertEqual(max_similar_indices([(sys.maxsize, sys.maxsize), (0, 0)],
                                              [(sys.maxsize - 1, sys.maxsize - 1), (sys.maxsize, sys.maxsize)]),
                         [(0, 0), (1, 1)])

    def test_min_values(self):
        self.assertEqual(max_similar_indices([(0, 0), (sys.minsize, sys.minsize)],
                                              [(0, 0), (sys.minsize + 1, sys.minsize + 1)]),
                         [(0, 0), (0, 1)])
