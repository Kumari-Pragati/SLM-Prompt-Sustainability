import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_move_zero(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zero([0, 0, 1, 2, 0]), [1, 2, 0, 0, 0])
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(move_zero([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])
        self.assertEqual(move_zero([]), [])

    def test_move_zero_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_move_zero_single_zero(self):
        self.assertEqual(move_zero([0]), [0])

    def test_move_zero_single_non_zero(self):
        self.assertEqual(move_zero([1]), [1])

    def test_move_zero_all_zeros(self):
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_move_zero_mixed(self):
        self.assertEqual(move_zero([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])
