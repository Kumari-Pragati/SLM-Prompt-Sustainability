import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]), [(5, 6), (7, 8)])

    def test_edge_case(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_boundary_case(self):
        self.assertEqual(max_similar_indices([(1, 2)], [(5, 6)]), [(5, 6)])

    def test_corner_case(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (4, 3)]), [(5, 6), (4, 4)])
