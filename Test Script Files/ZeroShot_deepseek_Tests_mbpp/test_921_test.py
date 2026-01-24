import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_chunk_tuples_with_even_division(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 3
        expected_result = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_chunk_tuples_with_odd_division(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 3
        expected_result = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_chunk_tuples_with_large_N(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 10
        expected_result = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_chunk_tuples_with_small_N(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 1
        expected_result = [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)

    def test_chunk_tuples_with_empty_tup(self):
        test_tup = ()
        N = 3
        expected_result = []
        self.assertEqual(chunk_tuples(test_tup, N), expected_result)
