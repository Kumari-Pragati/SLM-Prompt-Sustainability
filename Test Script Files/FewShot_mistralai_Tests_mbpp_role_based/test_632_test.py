import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(move_zero([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])

    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_single_element(self):
        self.assertEqual(move_zero([0]), [0])

    def test_all_zero(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(move_zero([-1, 0, -2, 0, -3]), [-1, -2, -3, 0, 0])

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(move_zero([1, 0, -2, 0, 3]), [1, -2, 3, 0, 0])

    def test_list_with_duplicate_zero(self):
        self.assertEqual(move_zero([1, 0, 0, 2, 0, 0, 3]), [1, 2, 3, 0, 0, 0, 0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            move_zero(1.5)
