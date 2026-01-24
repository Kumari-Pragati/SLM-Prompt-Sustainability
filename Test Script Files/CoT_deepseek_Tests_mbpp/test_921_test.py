import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(chunk_tuples(('a', 'b', 'c', 'd', 'e'), 2), [('a', 'b'), ('c', 'd'), ('e',)])

    def test_typical_case_with_odd_length(self):
        self.assertEqual(chunk_tuples(('a', 'b', 'c', 'd', 'e', 'f'), 2), [('a', 'b'), ('c', 'd'), ('e', 'f')])

    def test_with_large_N(self):
        self.assertEqual(chunk_tuples(('a', 'b', 'c', 'd', 'e'), 10), [('a', 'b', 'c', 'd', 'e',)])

    def test_with_zero_N(self):
        self.assertEqual(chunk_tuples(('a', 'b', 'c', 'd', 'e'), 0), [])

    def test_with_negative_N(self):
        with self.assertRaises(ValueError):
            chunk_tuples(('a', 'b', 'c', 'd', 'e'), -1)

    def test_with_empty_tuple(self):
        self.assertEqual(chunk_tuples((), 2), [])

    def test_with_empty_tuple_and_zero_N(self):
        self.assertEqual(chunk_tuples((), 0), [])

    def test_with_empty_tuple_and_negative_N(self):
        with self.assertRaises(ValueError):
            chunk_tuples((), -1)
