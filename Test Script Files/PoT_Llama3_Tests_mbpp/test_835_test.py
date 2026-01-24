import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_typical(self):
        self.assertAlmostEqual(slope(1, 2, 3, 4), 1.0)
        self.assertAlmostEqual(slope(2, 4, 4, 6), 1.0)
        self.assertAlmostEqual(slope(-1, -2, 1, 0), -1.0)

    def test_edge(self):
        self.assertAlmostEqual(slope(1, 1, 1, 1), float('inf'))
        self.assertAlmostEqual(slope(1, 1, 2, 1), 0.0)
        self.assertAlmostEqual(slope(1, 1, 1, 2), float('-inf'))

    def test_invalid(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            slope('a', 'b', 'c', 'd')
