import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(parabola_focus(1, -3, 2), (1.5, 0.5))

    def test_boundary_conditions(self):
        self.assertEqual(parabola_focus(1, 0, 0), (0, 1))
        self.assertEqual(parabola_focus(1, -2, 1), (1, 0))

    def test_edge_conditions(self):
        self.assertEqual(parabola_focus(1, -1, 0), (0.5, 0.5))
        self.assertEqual(parabola_focus(1, 0, -1), (0, 1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_focus("a", 1, 2)
        with self.assertRaises(TypeError):
            parabola_focus(1, "b", 2)
        with self.assertRaises(TypeError):
            parabola_focus(1, 2, "c")
