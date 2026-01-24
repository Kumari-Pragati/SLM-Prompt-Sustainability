import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(chunk_tuples([], 2), [])

    def test_single_element(self):
        self.assertListEqual(chunk_tuples([1], 1), [(1,)])
        self.assertListEqual(chunk_tuples([1], 2), [(1,)])

    def test_simple_list(self):
        self.assertListEqual(chunk_tuples([1, 2, 3, 4], 2), [(1, 2), (3, 4)])
        self.assertListEqual(chunk_tuples([1, 2, 3, 4], 3), [(1, 2, 3), (4,)])

    def test_long_list(self):
        long_list = [i for i in range(1, 11)]
        self.assertListEqual(chunk_tuples(long_list, 2), [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)])
        self.assertListEqual(chunk_tuples(long_list, 3), [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10,)])

    def test_negative_N(self):
        with self.assertRaises(ValueError):
            chunk_tuples([1, 2, 3], -1)

    def test_N_greater_than_list_length(self):
        with self.assertRaises(ValueError):
            chunk_tuples([1, 2, 3], 4)
