import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_chunk_tuples(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 3
        expected_output = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_chunk_tuples_even_length(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8)
        N = 2
        expected_output = [(1, 2), (3, 4), (5, 6), (7, 8)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_chunk_tuples_single_element(self):
        test_tup = (1,)
        N = 1
        expected_output = [(1,)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_chunk_tuples_N_is_zero(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 0
        with self.assertRaises(ValueError):
            chunk_tuples(test_tup, N)

    def test_chunk_tuples_N_is_greater_than_length(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        N = 20
        with self.assertRaises(ValueError):
            chunk_tuples(test_tup, N)
