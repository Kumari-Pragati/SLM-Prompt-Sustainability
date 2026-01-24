import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(parabola_focus(1, 0, 1), (0, 1))
        self.assertAlmostEqual(parabola_focus(-1, 0, -1), (0, -1))
        self.assertAlmostEqual(parabola_focus(1, 2, 1), (1, 1))
        self.assertAlmostEqual(parabola_focus(-1, -2, -1), (-1, 1))

    def test_edge_cases(self):
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_focus(0, 0, 1), (None, None))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_focus(1, 1, 0), (None, None))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, parabola_focus, 0, 0, 'str')
        self.assertRaises(ValueError, parabola_focus, 0, 'str', 0)
        self.assertRaises(ValueError, parabola_focus, 'str', 0, 0)
