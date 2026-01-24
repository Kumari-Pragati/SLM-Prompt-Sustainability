import unittest
from mbpp_921_code import Tuple

from 921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(chunk_tuples([], 2), [])

    def test_single_element(self):
        self.assertListEqual(chunk_tuples([1], 2), [[1]])

    def test_two_elements(self):
        self.assertListEqual(chunk_tuples([1, 2], 2), [[1, 2]])

    def test_three_elements(self):
        self.assertListEqual(chunk_tuples([1, 2, 3], 2), [[1, 2], [3]])

    def test_four_elements(self):
        self.assertListEqual(chunk_tuples([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_five_elements(self):
        self.assertListEqual(chunk_tuples([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_negative_N(self):
        with self.assertRaises(ValueError):
            chunk_tuples([1, 2, 3], -1)

    def test_N_greater_than_length(self):
        with self.assertRaises(ValueError):
            chunk_tuples([1, 2, 3], 4)
