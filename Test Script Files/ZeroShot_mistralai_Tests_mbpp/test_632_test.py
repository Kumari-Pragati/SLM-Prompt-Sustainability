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

    def test_list_with_duplicates(self):
        self.assertEqual(move_zero([0, 0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0, 0])
