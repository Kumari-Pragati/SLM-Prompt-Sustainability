import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_parabola_vertex_basic(self):
        self.assertAlmostEqual(parabola_vertex(1, 4, 1), (-2, 0))
        self.assertAlmostEqual(parabola_vertex(-2, -5, 3), (1, 2))
        self.assertAlmostEqual(parabola_vertex(0, 0, 1), (0, 1))
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, 0))
        self.assertRaises(ValueError, parabola_vertex, 0, 0, 0)
        self.assertRaises(ValueError, parabola_vertex, 0, 'not_a_number', 0)
