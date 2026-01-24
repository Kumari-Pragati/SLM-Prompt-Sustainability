import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 2), [(1, 2), (3, 4), (5, 6)])
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 3), [(1, 2, 3), (4, 5, 6)])
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 1), [(1), (2), (3), (4), (5), (6)])

    def test_edge_case_empty_list(self):
        self.assertEqual(chunk_tuples([], 2), [])

    def test_edge_case_single_element(self):
        self.assertEqual(chunk_tuples([1], 2), [])

    def test_edge_case_single_element_N(self):
        self.assertEqual(chunk_tuples([1], 1), [(1)])

    def test_edge_case_N_zero(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 0), [])

    def test_edge_case_N_greater_than_length(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 7), [(1, 2, 3, 4, 5, 6)])
