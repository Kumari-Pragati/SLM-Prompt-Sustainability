import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (1, -1))

    def test_edge_case_a_zero(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(0, 2, 3)

    def test_edge_case_b_zero(self):
        self.assertAlmostEqual(parabola_focus(1, 0, 3), (1, 3))

    def test_edge_case_c_zero(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 0), (1, 2))

    def test_edge_case_a_negative(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_focus(-1, 2, 3)

    def test_edge_case_b_negative(self):
        self.assertAlmostEqual(parabola_focus(1, -2, 3), (1, 1))

    def test_edge_case_c_negative(self):
        self.assertAlmostEqual(parabola_focus(1, 2, -3), (1, 2))
