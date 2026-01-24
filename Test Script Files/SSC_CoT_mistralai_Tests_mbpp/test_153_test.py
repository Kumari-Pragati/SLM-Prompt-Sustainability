import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertAlmostEqual(parabola_vertex(1, 4, 16), (2, 8))
        self.assertAlmostEqual(parabola_vertex(-2, -8, 16), (-2, 8))
        self.assertAlmostEqual(parabola_vertex(3, -12, 48), (-4, 12))

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(0, 0, 1), (0, -1))
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, 1))
        self.assertAlmostEqual(parabola_vertex(1, 1, 0), (0, 0))

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, parabola_vertex, 0, 0, 0)
        self.assertRaises(ValueError, parabola_vertex, 0, 0, 1)
        self.assertRaises(ValueError, parabola_vertex, 1, 'not_a_number', 0)
