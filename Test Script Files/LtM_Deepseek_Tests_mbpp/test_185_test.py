import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_focus(1, -3, 2), (1.5, 1.0))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(0, -3, 2)

    def test_negative_a(self):
        self.assertEqual(parabola_focus(-1, -3, 2), (-1.5, 1.0))

    def test_large_numbers(self):
        self.assertEqual(parabola_focus(1000000, -3000000, 2000000), (3000.0, 1000001.0))

    def test_small_numbers(self):
        self.assertEqual(parabola_focus(0.000001, -0.000003, 0.000002), (-150000.0, 1.0))

    def test_negative_c(self):
        self.assertEqual(parabola_focus(1, -3, -2), (1.5, -1.0))
