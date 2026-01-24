import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 2), [(1, 2), (3, 4), (5,)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 3), [(1, 2, 3), (4, 5,)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5), 1), [(1), (2), (3), (4), (5)])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(chunk_tuples((1, 2, 3), 2), [(1, 2), (3,)])
        self.assertListEqual(chunk_tuples((1, 2, 3), 1), [(1), (2), (3)])
        self.assertListEqual(chunk_tuples((1,), 2), [(1,)])
        self.assertListEqual(chunk_tuples((1, 2, 3), 4), [])

    def test_complex_scenarios(self):
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 3), [(1, 2, 3), (4, 5, 6), (7, 8,)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 4), [(1, 2, 3, 4), (5, 6, 7, 8)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 5), [(1, 2, 3, 4, 5), (6, 7, 8)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 6), [(1, 2, 3, 4, 5, 6), (7, 8)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 7), [(1, 2, 3, 4, 5, 6, 7)])
        self.assertListEqual(chunk_tuples((1, 2, 3, 4, 5, 6, 7, 8), 8), [(1, 2, 3, 4, 5, 6, 7, 8)])
