import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_move_zero(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(move_zero([]), [])
        self.assertEqual(move_zero([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(move_zero([5, 0, 6, 0, 7]), [5, 6, 7, 0, 0])
