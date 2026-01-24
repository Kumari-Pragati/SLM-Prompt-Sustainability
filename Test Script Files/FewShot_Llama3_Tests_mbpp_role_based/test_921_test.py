import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 3
        expected_output = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_edge_case_N_is_1(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 1
        expected_output = [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_edge_case_N_is_equal_to_length(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 10
        expected_output = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_edge_case_N_is_greater_than_length(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 20
        expected_output = [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)
