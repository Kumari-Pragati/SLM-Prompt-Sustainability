import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_list_with_zero(self):
        self.assertEqual(move_zero([0, 1, 2, 0, 3]), [1, 2, 0, 0, 3])

    def test_list_without_zero(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_multiple_zero(self):
        self.assertEqual(move_zero([0, 0, 1, 2, 0, 3, 0]), [1, 2, 0, 0, 3, 0])

    def test_list_with_negative_numbers(self):
        self.assertEqual(move_zero([-1, 0, 2, -3, 0]), [-1, 2, -3, 0, 0])
