import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):

    def test_parabola_directrix_with_positive_values(self):
        self.assertEqual(parabola_directrix(1, 2, 10), 20)
        self.assertEqual(parabola_directrix(2, 3, 12), 24)
        self.assertEqual(parabola_directrix(3, 4, 16), 32)

    def test_parabola_directrix_with_zero_values(self):
        self.assertRaises(ValueError, parabola_directrix, 0, 0, 0)
        self.assertRaises(ValueError, parabola_directrix, 0, 2, 0)
        self.assertRaises(ValueError, parabola_directrix, 2, 0, 0)

    def test_parabola_directrix_with_negative_values(self):
        self.assertEqual(parabola_directrix(-1, -2, -10), 20)
        self.assertEqual(parabola_directrix(-2, -3, -12), 24)
        self.assertEqual(parabola_directrix(-3, -4, -16), 32)
