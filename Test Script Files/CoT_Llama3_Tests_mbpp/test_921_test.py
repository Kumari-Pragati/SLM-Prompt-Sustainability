import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 2), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case_single_element(self):
        self.assertEqual(chunk_tuples((1,), 1), [(1,)])

    def test_edge_case_single_element_with_N_1(self):
        self.assertEqual(chunk_tuples((1,), 1), [(1,)])

    def test_edge_case_empty_input(self):
        self.assertEqual(chunk_tuples([], 2), [])

    def test_edge_case_N_is_zero(self):
        with self.assertRaises(ValueError):
            chunk_tuples((1, 2, 3), 0)

    def test_edge_case_N_is_greater_than_input_length(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 4), [(1, 2, 3)])

    def test_edge_case_N_is_greater_than_input_length_with_N_greater_than_input_length(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 5), [(1, 2, 3)])
