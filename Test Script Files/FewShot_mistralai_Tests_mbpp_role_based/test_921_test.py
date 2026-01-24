import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 2), [(1, 2), (3, 4), (5,)])
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 3), [(1, 2, 3), (4, 5,)])
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 4), [(1, 2, 3, 4)])
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5), 1), [(1), (2), (3), (4), (5)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 1), [(1), (2), (3)])
        self.assertEqual(chunk_tuples((1, 2, 3), 2), [(1, 2), (3,)])
        self.assertEqual(chunk_tuples((1, 2, 3), 3), [(1, 2, 3)])
        self.assertEqual(chunk_tuples((1, 2, 3), 4), [(1, 2, 3)])
        self.assertEqual(chunk_tuples((1, 2, 3), 5), [(1, 2, 3)])
        self.assertEqual(chunk_tuples((), 1), [])
        self.assertEqual(chunk_tuples((1,), 1), [(1,)])
        self.assertEqual(chunk_tuples((1, 2), 1), [(1,), (2,)])
