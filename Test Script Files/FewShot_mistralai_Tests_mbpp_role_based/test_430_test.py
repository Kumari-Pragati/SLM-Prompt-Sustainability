import unittest
from mbpp_430_code import parabola_directrix

class TestParabolaDirectrix(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(parabola_directrix(1, 2, 3), 12)
        self.assertEqual(parabola_directrix(1, 4, 16), 0)

    def test_zero_and_negative_numbers(self):
        self.assertRaises(ValueError, parabola_directrix, 1, 2, 0)
        self.assertRaises(ValueError, parabola_directrix, 1, 2, -1)
        self.assertEqual(parabola_directrix(1, 2, -2), 8)

    def test_negative_b_and_c(self):
        self.assertRaises(ValueError, parabola_directrix, 1, -2, 3)
        self.assertRaises(ValueError, parabola_directrix, 1, -2, -3)
