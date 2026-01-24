import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(parabola_directrix(1, 2, 3), 12)
        self.assertEqual(parabola_directrix(2, 3, 4), 16)
        self.assertEqual(parabola_directrix(3, 4, 5), 20)

    def test_edge_cases(self):
        self.assertEqual(parabola_directrix(0, 0, 1), 3)
        self.assertEqual(parabola_directrix(1, 0, 1), -3)
        self.assertEqual(parabola_directrix(1, 1, 0), 0)

    def test_negative_coefficients(self):
        self.assertEqual(parabola_directrix(-1, 2, 3), -12)
        self.assertEqual(parabola_directrix(1, -2, 3), -24)
        self.assertEqual(parabola_directrix(1, 2, -3), -12)

    def test_zero_coefficients(self):
        self.assertEqual(parabola_directrix(0, 0, 0), None)
        self.assertEqual(parabola_directrix(0, 0, 1), 3)
        self.assertEqual(parabola_directrix(0, 1, 0), -3)
