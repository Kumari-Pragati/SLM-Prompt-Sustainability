import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 2), [(1, 2), (3, 4), (5,)])

    def test_edge_case_empty_tuple(self):
        self.assertEqual(chunk_tuples((), 2), [])

    def test_edge_case_N_equals_zero(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 0), [])

    def test_boundary_case_N_equals_one(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 1), [(1,), (2,), (3,), (4,), (5,)])

    def test_boundary_case_tuple_length_equals_N(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 5), [(1, 2, 3, 4, 5)])

    def test_complex_case_tuple_length_greater_than_N(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 2), [(1, 2), (3, 4), (5, 6)])
