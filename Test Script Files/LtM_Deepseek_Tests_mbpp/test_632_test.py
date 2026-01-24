import unittest
from mbpp_632_code import move_zero

class TestMoveZero(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(move_zero([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([1, 0]), [1, 0])

    def test_edge_conditions(self):
        self.assertEqual(move_zero([]), [])
        self.assertEqual(move_zero([1]), [1])
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])

    def test_complex_cases(self):
        self.assertEqual(move_zero([0, 1, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])
        self.assertEqual(move_zero([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(move_zero([1, 2, 3, 4]), [1, 2, 3, 4])
