import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(chunk_tuples((1, 2, 3, 4, 5, 6), 2), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case1(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 1), [(1,), (2,), (3,)])

    def test_edge_case2(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 3), [(1, 2, 3)])

    def test_edge_case3(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 4), [(1, 2, 3)])

    def test_edge_case4(self):
        self.assertEqual(chunk_tuples((1, 2, 3), 0), [])

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            chunk_tuples(None, 2)

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            chunk_tuples("test", 2)
