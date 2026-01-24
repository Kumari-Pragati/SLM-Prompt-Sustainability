import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_single_zero(self):
        self.assertEqual(move_zero([0]), [0])

    def test_single_non_zero(self):
        self.assertEqual(move_zero([1]), [1])

    def test_multiple_zeros(self):
        self.assertEqual(move_zero([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])

    def test_multiple_non_zeros(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_duplicate_zeros(self):
        self.assertEqual(move_zero([0, 0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0, 0])

    def test_list_with_duplicate_non_zeros(self):
        self.assertEqual(move_zero([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_list_with_only_zeros(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_list_with_only_non_zeros(self):
        self.assertEqual(move_zero([1, 1, 1]), [1, 1, 1])

    def test_list_with_long_sequence_of_zeros(self):
        self.assertEqual(move_zero([0] * 100 + [1]), [1] + [0] * 100)

    def test_list_with_long_sequence_of_non_zeros(self):
        self.assertEqual(move_zero([1] * 100 + [0]), [1] * 100)
