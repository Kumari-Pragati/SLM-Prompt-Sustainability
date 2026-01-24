import unittest
from mbpp_921_code import chunk_tuples

class TestChunkTuples(unittest.TestCase):
    def test_typical_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 3
        expected_output = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_boundary_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 10
        expected_output = [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_edge_case(self):
        test_tup = ()
        N = 3
        expected_output = []
        self.assertEqual(chunk_tuples(test_tup, N), expected_output)

    def test_invalid_input(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        N = 'three'
        with self.assertRaises(TypeError):
            chunk_tuples(test_tup, N)
