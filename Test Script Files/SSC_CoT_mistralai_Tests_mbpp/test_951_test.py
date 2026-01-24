import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]), [(1, 5), (2, 6)])
        self.assertEqual(max_similarIndices([(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]), [(0, 0), (1, 1)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_similarIndices([], []), [])
        self.assertEqual(max_similarIndices([(1, 2)], []), [])
        self.assertEqual(max_similarIndices([], [(1, 2)]), [])
        self.assertEqual(max_similarIndices([(1, 2)], [(1, 2), (1, 2)]), [(1, 2), (1, 2)])
        self.assertEqual(max_similarIndices([(1, 2), (1, 2)], [(1, 2), (1, 2)]), [(1, 2), (1, 2)])
        self.assertEqual(max_similarIndices([(1, 2), (1, 2)], [(2, 1), (2, 1)]), [(1, 2), (2, 1)])
        self.assertEqual(max_similarIndices([(1, 2), (1, 2)], [(2, 1), (1, 2)]), [(1, 2), (2, 1)])
