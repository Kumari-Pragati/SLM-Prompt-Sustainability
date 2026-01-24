import unittest
from mbpp_632_code import range
from six.moves import xrange

from move_zero import move_zero

class TestMoveZero(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(move_zero([1, 0, 2, 0, 3, 0, 4]), [1, 2, 3, 4, 0, 0, 0])
        self.assertEqual(move_zero([0, 1, 2, 0, 3]), [1, 2, 3, 0, 0])
        self.assertEqual(move_zero([0, 0, 1, 0, 2]), [1, 2, 0, 0, 0])
        self.assertEqual(move_zero([0, 0, 0, 1, 0, 2]), [1, 2, 0, 0, 0, 0])
        self.assertEqual(move_zero([0, 0, 0, 0, 1]), [1, 0, 0, 0, 0])

    def test_edge_cases(self):
        self.assertEqual(move_zero([]), [])
        self.assertEqual(move_zero([1]), [1])
        self.assertEqual(move_zero([0]), [0])
        self.assertEqual(move_zero([1, 0]), [1, 0])
        self.assertEqual(move_zero([0, 1]), [1, 0])

    def test_boundary_conditions(self):
        self.assertEqual(move_zero(range(10)), list(range(10)))
        self.assertEqual(move_zero(xrange(10)), list(xrange(10)))
        self.assertEqual(move_zero(list(range(-10, 10))), list(range(-10, 10)))
        self.assertEqual(move_zero(list(xrange(-10, 10))), list(xrange(-10, 10)))

    def test_complex_cases(self):
        self.assertEqual(move_zero([0, 1, 0, 1, 0, 1]), [1, 1, 0, 1, 0, 0])
        self.assertEqual(move_zero([1, 0, 1, 0, 1, 0]), [1, 1, 1, 0, 0, 0])
        self.assertEqual(move_zero([0, 1, 0, 1, 0, 1, 0]), [1, 1, 1, 0, 0, 0, 0])
        self.assertEqual(move_zero([0, 1, 0, 1, 0, 1, 0, 1]), [1, 1, 1, 0, 0, 0, 0, 1])
