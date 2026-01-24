import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_parabola_focus(self):
        self.assertAlmostEqual(parabola_focus(1, 2, 3), (-1, 0.5))
        self.assertAlmostEqual(parabola_focus(2, 3, 4), (-1.5, 0.75))
        self.assertAlmostEqual(parabola_focus(3, 4, 5), (-2, 1))

    def test_parabola_focus_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_focus('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_focus(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_focus(1, 2, 'c')
