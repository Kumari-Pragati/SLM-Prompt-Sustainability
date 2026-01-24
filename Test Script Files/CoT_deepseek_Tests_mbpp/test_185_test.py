import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_focus(1, -3, 2), (1.5, 1.0))

    def test_negative_coefficients(self):
        self.assertEqual(parabola_focus(-1, 3, -2), (-1.5, -1.0))

    def test_zero_coefficients(self):
        self.assertEqual(parabola_focus(0, 0, 0), (0, 0))

    def test_large_coefficients(self):
        self.assertEqual(parabola_focus(1000, -2000, 1000), (100.0, 100.0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_focus("a", "b", "c")
