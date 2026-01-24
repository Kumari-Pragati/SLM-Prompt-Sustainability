import unittest
from mbpp_185_code import parabola_focus

class TestParabolaFocus(unittest.TestCase):

    def test_typical_case(self):
        self.assertTupleEqual(parabola_focus(1, -3, 2), (1.5, 1.0))

    def test_boundary_case(self):
        self.assertTupleEqual(parabola_focus(0, 0, 0), (0, 0))

    def test_edge_case(self):
        self.assertTupleEqual(parabola_focus(1, 0, 0), (0, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parabola_focus("a", "b", "c")
