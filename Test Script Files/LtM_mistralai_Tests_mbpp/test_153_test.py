import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 3), (-1, 1))
        self.assertAlmostEqual(parabola_vertex(-1, 2, 3), (1, 1))
        self.assertAlmostEqual(parabola_vertex(1, -2, 3), (1, -1))
        self.assertAlmostEqual(parabola_vertex(-1, -2, 3), (-1, -1))

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(0, 0, 1), (0, 1))
        self.assertAlmostEqual(parabola_vertex(0, 1, 0), (0, -1))
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, None))
        self.assertAlmostEqual(parabola_vertex(-1, 0, 0), (0, None))

    def test_complex_inputs(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, -4), (-2, 2))
        self.assertAlmostEqual(parabola_vertex(-1, 2, -4), (2, 2))
        self.assertAlmostEqual(parabola_vertex(1, -2, -4), (-2, -2))
        self.assertAlmostEqual(parabola_vertex(-1, -2, -4), (2, -2))
