import unittest
from mbpp_632_code import range
from six.moves import zip_longest

from move_zero import move_zero

class TestMoveZero(unittest.TestCase):

    def test_typical_cases(self):
        self.assertListEqual(move_zero([0, 1, 0, 2, 3, 0, 4, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0])
        self.assertListEqual(move_zero([0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0])
        self.assertListEqual(move_zero([0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0])
        self.assertListEqual(move_zero([0, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5]), [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_edge_and_boundary_cases(self):
        self.assertListEqual(move_zero([]), [])
        self.assertListEqual(move_zero([1]), [1])
        self.assertListEqual(move_zero([0]), [0])
        self.assertListEqual(move_zero([0, 0]), [0, 0])
        self.assertListEqual(move_zero([1, 0]), [1, 0])
        self.assertListEqual(move_zero([0, 1]), [1, 0])
        self.assertListEqual(move_zero([0, 0, 1]), [1, 0, 0])
        self.assertListEqual(move_zero([1, 0, 0]), [1, 0])
