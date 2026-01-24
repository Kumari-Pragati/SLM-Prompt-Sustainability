import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(move_zero([1, 2, 0, 3, 4]), [1, 2, 3, 4, 0])

    def test_edge_case_zero_at_start(self):
        self.assertEqual(move_zero([0, 1, 2, 3, 4]), [1, 2, 3, 4, 0])

    def test_edge_case_zero_at_end(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 0]), [1, 2, 3, 4, 0])

    def test_edge_case_all_zeros(self):
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_edge_case_all_non_zeros(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_single_zero(self):
        self.assertEqual(move_zero([1, 0, 2]), [1, 2, 0])

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(move_zero([1, 0, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            move_zero(123)

    def test_invalid_input_non_integer_zero(self):
        with self.assertRaises(TypeError):
            move_zero([1, 2, 'zero', 4])
