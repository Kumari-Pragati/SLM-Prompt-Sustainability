import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_Position([1, 2, 3, 4], 3, 2), 3)
        self.assertEqual(get_Position([5, 10, 15, 20], 4, 5), 4)
        self.assertEqual(get_Position([-1, 0, 1, 2], 4, 1), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Position([], 1, 1), 1)
        self.assertEqual(get_Position([1], 1, 1), 1)
        self.assertEqual(get_Position([1, 2], 1, 1), 1)
        self.assertEqual(get_Position([1, 2, 3], 1, 1), 1)
        self.assertEqual(get_Position([1, 2, 3], 0, 1), 1)
        self.assertEqual(get_Position([1, 2, 3], 4, 1), 1)
        self.assertEqual(get_Position([1, 2, 3], 3, 0), 1)
        self.assertEqual(get_Position([1, 2, 3], 3, 2), 3)
        self.assertEqual(get_Position([1, 2, 3], 3, 3), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_Position, 'string', 1, 1)
        self.assertRaises(TypeError, get_Position, [1], 1, 'int')
        self.assertRaises(TypeError, get_Position, [1, 2], 'int', 1)
        self.assertRaises(TypeError, get_Position, [1, 2], 1, 'float')
        self.assertRaises(ValueError, get_Position, [1, 2], -1, 1)
        self.assertRaises(ValueError, get_Position, [1, 2], 1, -1)
        self.assertRaises(ValueError, get_Position, [1, 2], 0, 0)
