import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (1, 1.5))
        self.assertAlmostEqual(parabola_focus(2, 3, 4), (2, 2.5))
        self.assertAlmostEqual(parabola_focus(3, 4, 5), (3, 3.5))

    def test_edge_cases(self):
        self.assertAlmostEqual(parabola_focus(0, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_focus(1, 0, 0), (1, 0))
        self.assertAlmostEqual(parabola_focus(0, 1, 0), (0, 0.5))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_focus('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_focus(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_focus(1, 2, 'c')
