import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(parabola_directrix(1, 2, 3), -12, delta=1)
        self.assertAlmostEqual(parabola_directrix(2, 3, 10), 16, delta=1)
        self.assertAlmostEqual(parabola_directrix(3, 4, 13), 28, delta=1)

    def test_zero_coefficients(self):
        self.assertAlmostEqual(parabola_directrix(0, 0, 0), None)
        self.assertAlmostEqual(parabola_directrix(0, 1, 0), None)
        self.assertAlmostEqual(parabola_directrix(1, 0, 0), None)

    def test_negative_numbers(self):
        self.assertAlmostEqual(parabola_directrix(-1, -2, -3), 12, delta=1)
        self.assertAlmostEqual(parabola_directrix(-2, -3, -10), -16, delta=1)
        self.assertAlmostEqual(parabola_directrix(-3, -4, -13), -28, delta=1)

    def test_edge_cases(self):
        self.assertAlmostEqual(parabola_directrix(1, 0, 1), None)
        self.assertAlmostEqual(parabola_directrix(0, 1, 1), None)
        self.assertAlmostEqual(parabola_directrix(1, 1, 0), None)

    def test_invalid_input(self):
        self.assertRaises(TypeError, parabola_directrix, 'a', 1, 2)
        self.assertRaises(TypeError, parabola_directrix, 1, 'b', 2)
        self.assertRaises(TypeError, parabola_directrix, 1, 2, 'c')
