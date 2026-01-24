import unittest
from mbpp_185_code import sqrt
from 185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_parabola_focus_simple(self):
        self.assertAlmostEqual(parabola_focus(1, 0, 1), (0, 1))

    def test_parabola_focus_positive(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1, 5))

    def test_parabola_focus_negative(self):
        self.assertAlmostEqual(parabola_focus(1, -2, 3), (1, 5))

    def test_parabola_focus_zero_a(self):
        self.assertAlmostEqual(parabola_focus(0, 1, 1), (None, None))

    def test_parabola_focus_zero_c(self):
        self.assertAlmostEqual(parabola_focus(1, 1, 0), (None, None))

    def test_parabola_focus_invalid_a(self):
        with self.assertRaises(ValueError):
            parabola_focus(0, 1, 1, 'invalid')

    def test_parabola_focus_invalid_b(self):
        with self.assertRaises(ValueError):
            parabola_focus(1, 0, 1, 'invalid')

    def test_parabola_focus_invalid_c(self):
        with self.assertRaises(ValueError):
            parabola_focus(1, 1, 0, 'invalid')
