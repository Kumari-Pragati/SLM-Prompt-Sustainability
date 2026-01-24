import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1, 5))
        self.assertAlmostEqual(parabola_focus(-1, -2, -3), (1, -5))

    def test_zero_values(self):
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (0, 1))
        self.assertAlmostEqual(parabola_focus(0, 0, 1), (0, 1))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), (0, 1))

    def test_negative_values(self):
        self.assertAlmostEqual(parabola_focus(-1, 2, 3), (-1, -5))
        self.assertAlmostEqual(parabola_focus(1, -2, 3), (1, -5))
        self.assertAlmostEqual(parabola_focus(1, 2, -3), (1, 5))

    def test_invalid_input_a(self):
        with self.assertRaises(ValueError):
            parabola_focus(0, 2, 3)

    def test_invalid_input_b(self):
        with self.assertRaises(ValueError):
            parabola_focus(1, 0, 3)

    def test_invalid_input_c(self):
        with self.assertRaises(ValueError):
            parabola_focus(1, 2, 0)
