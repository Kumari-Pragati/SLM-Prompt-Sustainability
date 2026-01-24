import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(move_zero([1, 2, 0, 3, 4]), [1, 2, 3, 4, 0])
        self.assertEqual(move_zero([0, 1, 2, 3, 4]), [1, 2, 3, 4, 0])
        self.assertEqual(move_zero([5, 0, 0, 0, 6]), [5, 6, 0, 0, 0])

    def test_edge(self):
        self.assertEqual(move_zero([]), [])
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([1]), [1])

    def test_complex(self):
        self.assertEqual(move_zero([1, 2, 0, 0, 3, 4, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0])
        self.assertEqual(move_zero([0, 0, 0, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0])
