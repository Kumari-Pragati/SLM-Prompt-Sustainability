import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 2), [(1, 2), (3, 4), (5,)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 3), [(1, 2, 3), (4, 5,)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 4), [(1, 2, 3, 4)])

    def test_edge_input(self):
        self.assertListEqual(chunk_tuples((1, 2, 3), 2), [(1, 2), (3,)])
        self.assertListEqual(chunk_tuples((1, 2, 3), 1), [(1,), (2,), (3,)])
        self.assertListEqual(chunk_tuples((1, 2), 2), [(1, 2)])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            chunk_tuples((1, 2, 3), 0)
        with self.assertRaises(TypeError):
            chunk_tuples(1, 2)
