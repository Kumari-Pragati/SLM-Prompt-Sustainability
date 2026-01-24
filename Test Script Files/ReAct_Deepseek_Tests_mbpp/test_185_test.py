import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_focus(1, -3, 2), (1.5, 1.0))

    def test_negative_coefficients(self):
        self.assertEqual(parabola_focus(-1, 3, -2), (-1.5, -1.0))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(0, 1, 1)

    def test_large_numbers(self):
        self.assertEqual(parabola_focus(1000, -3000, 2000), (30.0, 20.0))

    def test_negative_b(self):
        self.assertEqual(parabola_focus(1, -5, 2), (2.5, 1.0))

    def test_negative_c(self):
        self.assertEqual(parabola_focus(1, -3, -2), (1.5, -1.0))

    def test_zero_b_and_c(self):
        self.assertEqual(parabola_focus(1, 0, 0), (0, 0.5))

    def test_zero_b(self):
        self.assertEqual(parabola_focus(1, 0, 2), (0, 1.0))

    def test_zero_c(self):
        self.assertEqual(parabola_focus(1, -3, 0), (1.5, 0))
