import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1.0, 1.0))
        self.assertAlmostEqual(parabola_focus(-1, 2, 3), (1.0, 1.0))
        self.assertAlmostEqual(parabola_focus(1, -2, 3), (-1.0, -1.0))
        self.assertAlmostEqual(parabola_focus(-1, -2, 3), (1.0, -1.0))

    def test_edge_input(self):
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_focus(0, 0, 1), (None, None))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), (0.0, None))

    def test_complex_input(self):
        self.assertAlmostEqual(parabola_focus(1, 2, -4), (-2.0, 5.0))
        self.assertAlmostEqual(parabola_focus(-1, 2, -4), (2.0, 5.0))
        self.assertAlmostEqual(parabola_focus(1, -2, -4), (-2.0, -5.0))
        self.assertAlmostEqual(parabola_focus(-1, -2, -4), (2.0, -5.0))
