import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_Position([1, 2, 3, 4], 4, 3), 4)
        self.assertEqual(get_Position([10, 20, 30, 40], 4, 10), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Position([0, 0, 0, 0], 4, 1), 4)
        self.assertEqual(get_Position([9, 9, 9, 9], 4, 1), 1)
        self.assertEqual(get_Position([1, 1, 1, 1], 1, 1), 1)
        self.assertEqual(get_Position([], 1, 1), None)
        self.assertEqual(get_Position([1], 1, 1), 1)

    def test_negative_input(self):
        self.assertRaises(ValueError, get_Position, [-1, -2, -3], 4, 3)
        self.assertRaises(ValueError, get_Position, [1, 2, 3], -4, 3)
        self.assertRaises(ValueError, get_Position, [1, 2, 3], 4, -3)
