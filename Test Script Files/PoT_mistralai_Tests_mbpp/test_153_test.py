import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(parabola_vertex(1, 4, 1), (-2, 1))
        self.assertAlmostEqual(parabola_vertex(-2, -8, 9), (2, 3))
        self.assertAlmostEqual(parabola_vertex(3, 12, -4), (-1, 2))

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_vertex(0, 0, 1), (None, None))
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (None, None))
        self.assertAlmostEqual(parabola_vertex(1, 1, 0), (None, None))
        self.assertAlmostEqual(parabola_vertex(1, 1, 1), (None, None))
