import unittest
from mbpp_378_code import move_first

class TestMoveFirst(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_first([1, 2, 3]), [3, 1, 2])
        self.assertEqual(move_first([0, 0, 0]), [0, 0, 0])
        self.assertEqual(move_first([1, 'a', 3]), ['a', 1, 3])

    def test_edge_case(self):
        self.assertEqual(move_first([]), [])
        self.assertEqual(move_first([None]), [None])
        self.assertEqual(move_first([1, 2, None]), [None, 1, 2])

    def test_corner_case(self):
        self.assertEqual(move_first([float('inf'), 2, float('-inf')]), [float('-inf'), float('inf'), 2])
        self.assertEqual(move_first([1, 'a', 2, 'a']), ['a', 1, 'a', 2])
