import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_single_zero(self):
        self.assertEqual(move_zero([0]), [0])

    def test_multiple_zeros(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_single_nonzero(self):
        self.assertEqual(move_zero([1]), [1])

    def test_multiple_nonzero(self):
        self.assertEqual(move_zero([1, 2, 3]), [1, 2, 3])

    def test_mixed_zeros_and_nonzero(self):
        self.assertEqual(move_zero([0, 1, 0, 2, 0]), [0, 1, 0, 2, 0])

    def test_list_with_duplicates(self):
        self.assertEqual(move_zero([0, 0, 1, 1, 2, 2]), [0, 0, 1, 1, 2, 2])

    def test_list_with_zero_at_end(self):
        self.assertEqual(move_zero([1, 2, 0]), [1, 2, 0])

    def test_list_with_zero_at_start(self):
        self.assertEqual(move_zero([0, 1, 2]), [0, 1, 2])

    def test_list_with_zero_in_middle(self):
        self.assertEqual(move_zero([1, 0, 2]), [1, 0, 2])
