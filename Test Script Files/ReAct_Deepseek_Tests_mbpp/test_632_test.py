import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_no_zero_case(self):
        self.assertEqual(move_zero([1, 3, 12]), [1, 3, 12])

    def test_all_zero_case(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_empty_list_case(self):
        self.assertEqual(move_zero([]), [])

    def test_negative_numbers_case(self):
        self.assertEqual(move_zero([-1, 0, 3, -2]), [-1, 3, -2, 0])

    def test_mixed_numbers_case(self):
        self.assertEqual(move_zero([0, 1, -1, 0, 3, -2]), [1, -1, 3, -2, 0, 0])
