import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])
        self.assertEqual(move_first([0, 0, 0]), [0, 0, 0])
        self.assertEqual(move_first([1]), [1])

    def test_edge_cases(self):
        self.assertEqual(move_first([]), [])
        self.assertEqual(move_first([None]), [None])
        self.assertEqual(move_first([True]), [True])
        self.assertEqual(move_first([False]), [False])
        self.assertEqual(move_first([float('inf')]), [float('inf')])
        self.assertEqual(move_first([float('-inf')]), [float('-inf')])

    def test_complex_cases(self):
        self.assertEqual(move_first([0, 1, 2, 3]), [3, 0, 1, 2])
        self.assertEqual(move_first([0, 0, 1, 2, 3]), [3, 0, 0, 1, 2])
        self.assertEqual(move_first([0, 0, 0, 1, 2, 3]), [3, 0, 0, 0, 1, 2])
        self.assertEqual(move_first([0, 0, 0, 0, 1, 2, 3]), [3, 0, 0, 0, 0, 1, 2])
