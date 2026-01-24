import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_single_zero(self):
        self.assertEqual(move_zero([0]), [0])

    def test_single_non_zero(self):
        self.assertEqual(move_zero([1]), [1])

    def test_multiple_zeros_and_non_zeros(self):
        self.assertEqual(move_zero([0, 1, 0, 2, 3, 0, 4, 5]), [1, 2, 3, 4, 5, 0, 0, 0])

    def test_all_zeros(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_duplicate_zeros(self):
        self.assertEqual(move_zero([0, 0, 0, 1, 0, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0, 0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(move_zero([-1, 0, 2]), [-1, 2, 0])

    def test_invalid_input_type_list(self):
        with self.assertRaises(TypeError):
            move_zero(123)

    def test_invalid_input_type_element(self):
        with self.assertRaises(TypeError):
            move_zero(['a', 0, 'b'])
