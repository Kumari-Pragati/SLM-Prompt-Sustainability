import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_positive_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.6666666666666667)
        self.assertAlmostEqual(slope(-2, -3, -1, -4), -1.3333333333333333)

    def test_zero_slope(self):
        self.assertAlmostEqual(slope(1, 1, 2, 1), 0.0)
        self.assertAlmostEqual(slope(-1, -1, 0, -1), -1.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError:
            slope(1, 2, 1, 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            slope('a', 'b', 'c', 'd')
        with self.assertRaises(TypeError):
            slope(1, 2, 'c', 'd')
