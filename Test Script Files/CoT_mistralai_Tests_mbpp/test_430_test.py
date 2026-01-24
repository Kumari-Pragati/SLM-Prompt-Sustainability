import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(parabola_directrix(1, 2, 3), 12)
        self.assertEqual(parabola_directrix(2, 3, 10), 36)
        self.assertEqual(parabola_directrix(3, 4, 13), 52)

    def test_zero_values(self):
        self.assertEqual(parabola_directrix(1, 0, 1), 3)
        self.assertEqual(parabola_directrix(0, 2, 0), 1)
        self.assertEqual(parabola_directrix(0, 0, 1), 1)

    def test_negative_values(self):
        self.assertEqual(parabola_directrix(-1, -2, -3), 12)
        self.assertEqual(parabola_directrix(-2, -3, -10), 36)
        self.assertEqual(parabola_directrix(-3, -4, -13), 52)

    def test_edge_cases(self):
        self.assertEqual(parabola_directrix(0, 0, 0), 1)
        self.assertEqual(parabola_directrix(1, 1, 1), 3)
        self.assertEqual(parabola_directrix(1, 1, 4), 13)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, parabola_directrix, 0, 0, 0)
        self.assertRaises(ValueError, parabola_directrix, -1, 0, 0)
        self.assertRaises(ValueError, parabola_directrix, 1, -1, 0)
        self.assertRaises(ValueError, parabola_directrix, 1, 1, 0)
