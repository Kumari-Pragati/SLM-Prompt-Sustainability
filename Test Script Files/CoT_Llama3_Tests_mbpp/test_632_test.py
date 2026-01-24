import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_move_zero_typical(self):
        self.assertEqual(move_zero([1, 2, 0, 4, 5]), [1, 2, 4, 5, 0, 0])

    def test_move_zero_edge(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([]), [])

    def test_move_zero_invalid(self):
        with self.assertRaises(TypeError):
            move_zero(None)
        with self.assertRaises(TypeError):
            move_zero("hello")

    def test_move_zero_multiple_zeros(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 0, 4, 0]), [1, 3, 4, 0, 0, 0, 0])

    def test_move_zero_single_zero(self):
        self.assertEqual(move_zero([1, 0]), [1, 0])

    def test_move_zero_no_zeros(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
