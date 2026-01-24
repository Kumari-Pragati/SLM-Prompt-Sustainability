import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(slope(1, 2, 3, 4), 1.0)
        self.assertEqual(slope(-1, -2, 1, 0), -1.0)
        self.assertEqual(slope(0, 0, 0, 0), float('inf'))

    def test_edge_cases(self):
        self.assertRaises(ZeroDivisionError, slope, 1, 2, 1, 2)
        self.assertRaises(ZeroDivisionError, slope, 1, 2, 1, 1)
        self.assertEqual(slope(1, 2, 1, 2), float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            slope('a', 'b', 'c', 'd')
        with self.assertRaises(TypeError):
            slope(1, 2, 'c', 'd')
        with self.assertRaises(TypeError):
            slope(1, 2, 3, 'd')
