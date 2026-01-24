import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1.0, 0.5))

    def test_zero_coefficient(self):
        self.assertAlmostEqual(parabola_focus(0, 2, 3), (0.0, 1.5))

    def test_negative_coefficient(self):
        self.assertAlmostEqual(parabola_focus(-1, 2, 3), (1.0, 0.5))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            parabola_focus('a', 2, 3)

    def test_invalid_input_value(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(0, 0, 3)
