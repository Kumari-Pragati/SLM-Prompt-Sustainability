import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_zero([1, 2, 0, 3, 4]), [1, 2, 3, 4, 0])

    def test_edge_case_zero_list(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_edge_case_nonzero_list(self):
        self.assertEqual(move_zero([1, 2, 3]), [1, 2, 3])

    def test_edge_case_mixed_list(self):
        self.assertEqual(move_zero([1, 0, 2, 0, 3]), [1, 2, 3, 0, 0])

    def test_edge_case_empty_list(self):
        self.assertEqual(move_zero([]), [])

    def test_edge_case_single_zero(self):
        self.assertEqual(move_zero([0]), [0])

    def test_edge_case_single_nonzero(self):
        self.assertEqual(move_zero([1]), [1])

    def test_edge_case_all_zero(self):
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_edge_case_all_nonzero(self):
        self.assertEqual(move_zero([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
