import unittest
from mbpp_951_code import max_similar_indices

class TestMaxSimilarIndices(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_similar_indices([(1, 2), (3, 4)], [(5, 6), (7, 8)]), [(max(1, 5), max(2, 6)), (min(3, 7), min(4, 8))])

    def test_edge_case_1(self):
        self.assertEqual(max_similar_indices([(1, 2)], []), [])

    def test_edge_case_2(self):
        self.assertEqual(max_similar_indices([], [(1, 2)]), [])

    def test_edge_case_3(self):
        self.assertEqual(max_similar_indices([], []), [])

    def test_edge_case_4(self):
        self.assertEqual(max_similar_indices([(1, 2)], [(1, 2)]), [(1, 2)])

    def test_boundary_case_1(self):
        self.assertEqual(max_similar_indices([(0, 0)], [(1, 1)]), [(0, 0)])

    def test_boundary_case_2(self):
        self.assertEqual(max_similar_indices([(1, 1)], [(0, 0)]), [(1, 1)])
