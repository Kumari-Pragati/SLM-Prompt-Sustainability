import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1, 1.5))
        self.assertAlmostEqual(parabola_focus(-1, 2, 3), (1, 1.5))
        self.assertAlmostEqual(parabola_focus(1, -2, 3), (-1, -1.5))
        self.assertAlmostEqual(parabola_focus(-1, -2, 3), (1, -1.5))

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (0, 1))
        self.assertAlmostEqual(parabola_focus(0, 0, 1), (0, 0))
        self.assertAlmostEqual(parabola_focus(1e-10, 0, 0), (0, 1))
        self.assertAlmostEqual(parabola_focus(0, 1e-10, 0), (0, 1))
        self.assertAlmostEqual(parabola_focus(0, 0, 1e-10), (0, 1))
        self.assertAlmostEqual(parabola_focus(1, 2, 0), ((-2 / 4, None)))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), ((0, None)))
        self.assertAlmostEqual(parabola_focus(0, 1, 0), ((0, None)))
