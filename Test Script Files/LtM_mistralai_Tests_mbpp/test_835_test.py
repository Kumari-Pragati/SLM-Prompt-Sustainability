import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_simple_positive(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.6666666666666667)

    def test_simple_negative(self):
        self.assertAlmostEqual(slope(-1, -2, -3, -5), -1.6666666666666667)

    def test_zero_slope(self):
        self.assertAlmostEqual(slope(1, 1, 1, 1), 0.0)

    def test_edge_cases_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 0)

        with self.assertRaises(ZeroDivisionError):
            slope(0, 0, 1, 0)

    def test_edge_cases_same_x(self):
        self.assertAlmostEqual(slope(1, 2, 1, 2), 0.0)

    def test_edge_cases_opposite_signs(self):
        self.assertAlmostEqual(slope(1, 2, -1, -2), -1.0)
