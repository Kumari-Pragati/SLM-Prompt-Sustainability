import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 2), [(1, 2), (3, 4), (5,)])

    def test_edge_case_empty_input(self):
        self.assertEqual(chunk_tuples([], 2), [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(chunk_tuples((1,), 1), [(1,)])

    def test_edge_case_N_is_1(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 1), [(1,), (2,), (3,), (4,), (5,)])

    def test_edge_case_N_is_equal_to_length(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 5), [(1, 2, 3, 4, 5)])

    def test_edge_case_N_is_greater_than_length(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 6), [(1, 2, 3, 4, 5)])

    def test_edge_case_N_is_zero(self):
        with self.assertRaises(ValueError):
            chunk_tuples((1, 2, 3, 4, 5), 0)

    def test_edge_case_N_is_negative(self):
        with self.assertRaises(ValueError):
            chunk_tuples((1, 2, 3, 4, 5), -1)
