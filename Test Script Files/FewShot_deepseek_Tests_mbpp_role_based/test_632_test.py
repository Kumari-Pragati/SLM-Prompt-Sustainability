import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_no_zero(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_zero(self):
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_negative_numbers(self):
        self.assertEqual(move_zero([-1, 0, 2, -3, 0]), [-1, 2, -3, 0, 0])

    def test_mixed_numbers(self):
        self.assertEqual(move_zero([1, 0, 'a', 0, 2]), ['a', 2, 0, 0, 1])
