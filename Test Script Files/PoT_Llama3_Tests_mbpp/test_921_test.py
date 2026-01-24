import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 2), [[(1, 2), (3, 4), (5, 6)]])
    def test_edge_case_N_1(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 1), [[(1,)], [(2,)], [(3,)], [(4,)], [(5,)], [(6,)]])
    def test_edge_case_N_len(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 6), [[(1, 2, 3, 4, 5, 6)]])
    def test_edge_case_N_zero(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 0), [])
    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            chunk_tuples((1, 2, 3, 4, 5, 6), 'a')
    def test_invalid_input_non_positive(self):
        with self.assertRaises(ValueError):
            chunk_tuples((1, 2, 3, 4, 5, 6), -1)
