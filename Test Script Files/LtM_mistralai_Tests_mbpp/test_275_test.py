import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_Position([1, 2, 3], 3, 2), 3)
        self.assertEqual(get_Position([4, 5, 6], 3, 2), 1)
        self.assertEqual(get_Position([7, 8, 9], 3, 2), 1)

    def test_edge_input(self):
        self.assertEqual(get_Position([0, 0, 0], 3, 2), 3)
        self.assertEqual(get_Position([-1, -1, -1], 3, 2), 1)
        self.assertEqual(get_Position([1000000000, 1000000000, 1000000000], 3, 2), 1)

    def test_boundary_input(self):
        self.assertEqual(get_Position([0, 1, 2], 3, 1), 3)
        self.assertEqual(get_Position([1, 0, 2], 3, 1), 2)
        self.assertEqual(get_Position([1, 2, 0], 3, 1), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, get_Position, [-1, -2, -3], 3, 2)

    def test_zero_input(self):
        self.assertRaises(ValueError, get_Position, [0, 0, 0], 0, 2)
