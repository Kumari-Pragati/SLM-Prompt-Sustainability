import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 3
        expected_result = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_edge_case_N_equals_zero(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 0
        expected_result = []
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_edge_case_N_greater_than_length_of_tup(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 10
        expected_result = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_edge_case_empty_tup(self):
        test_tup = ()
        N = 3
        expected_result = []
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)
