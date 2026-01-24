import unittest
from mbpp_632_code import range
from six.moves import zip_longest

from move_zero import move_zero

class TestMoveZero(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(move_zero([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])
        self.assertEqual(move_zero([0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0])
        self.assertEqual(move_zero([0, 0, 1, 0, 2, 0, 3]), [1, 2, 3, 0, 0, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([1]), [1])
        self.assertEqual(move_zero([0, 1]), [1, 0])
        self.assertEqual(move_zero([1, 0]), [1, 0])
        self.assertEqual(move_zero([0, 0, 1]), [1, 0, 0])
        self.assertEqual(move_zero([1, 0, 0]), [1, 0])

    def test_boundary_cases(self):
        self.assertEqual(move_zero([-1, 0, 1]), [1, 0, -1])
        self.assertEqual(move_zero([1, -1, 0, 1]), [1, 1, 0, -1])
        self.assertEqual(move_zero([0, -1, 0, 1]), [1, -1, 0, 0])
        self.assertEqual(move_zero([-1, 0, 1, 0]), [1, 0, -1, 0])

    def test_special_cases(self):
        self.assertEqual(move_zero([0, 0, 0]), [0, 0, 0])
        self.assertEqual(move_zero([0, 0, 1]), [1, 0, 0])
        self.assertEqual(move_zero([1, 0, 0, 0]), [1, 0, 0, 0])
        self.assertEqual(move_zero([0, 1, 0, 0]), [1, 0, 0, 0])
