import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_no_zero_case(self):
        self.assertEqual(move_zero([1, 3, 12]), [1, 3, 12])

    def test_all_zero_case(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_negative_numbers(self):
        self.assertEqual(move_zero([-1, 0, -2, 0, -3]), [-1, -2, -3, 0, 0])

    def test_large_numbers(self):
        self.assertEqual(move_zero([1000, 0, 2000, 0, 3000]), [1000, 2000, 3000, 0, 0])

    def test_float_numbers(self):
        self.assertEqual(move_zero([1.5, 0, 2.5, 0, 3.5]), [1.5, 2.5, 3.5, 0, 0])

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            move_zero(['1', '0', '2', '0', '3'])
