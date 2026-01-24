import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 3), (-1, -1))

    def test_edge_cases(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(0, 1, 0), (0, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            parabola_vertex('a', 2, 3)
        with self.assertRaises(TypeError):
            parabola_vertex(1, 'b', 3)
        with self.assertRaises(TypeError):
            parabola_vertex(1, 2, 'c')

    def test_special_cases(self):
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(1, 1, 1), (1/2, 1/2))
