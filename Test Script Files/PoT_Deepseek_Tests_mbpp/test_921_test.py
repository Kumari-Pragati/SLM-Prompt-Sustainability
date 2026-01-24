import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 3),
                         [(1, 2, 3), (4, 5, 6), (7, 8, 9)])

    def test_edge_case_N_equals_zero(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 0), [])

    def test_boundary_case_N_equals_one(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 1),
                         [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)])

    def test_corner_case_N_greater_than_length_of_tup(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9), 10),
                         [(1, 2, 3, 4, 5, 6, 7, 8, 9,)])

    def test_corner_case_empty_tup(self):
        self.assertEqual(chunk_tuples((), 3), [])
