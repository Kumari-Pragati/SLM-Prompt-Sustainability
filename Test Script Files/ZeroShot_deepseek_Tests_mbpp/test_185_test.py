import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_positive_a(self):
        self.assertEqual(parabola_focus(1, -3, 2), (1.5, 2.0))

    def test_negative_a(self):
        self.assertEqual(parabola_focus(-1, 3, -2), (-0.5, -1.0))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(0, 1, 1)
