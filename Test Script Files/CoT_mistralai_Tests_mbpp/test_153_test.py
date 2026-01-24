import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(parabola_vertex(1, 4, 16), (2, 8))
        self.assertAlmostEqual(parabola_vertex(-2, -8, 16), (-2, 8))
        self.assertAlmostEqual(parabola_vertex(3, 9, 25), (1.5, 15))

    def test_zero_values(self):
        self.assertAlmostEqual(parabola_vertex(1, 0, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(0, 1, 0), (0, 0))
        self.assertAlmostEqual(parabola_vertex(0, 0, 1), (0, 0))

    def test_negative_discriminant(self):
        self.assertRaises(ValueError, parabola_vertex, 1, 4, -1)
        self.assertRaises(ValueError, parabola_vertex, -1, 4, 1)

    def test_zero_coefficient_a(self):
        self.assertRaises(ValueError, parabola_vertex, 0, 4, 1)
        self.assertRaises(ValueError, parabola_vertex, -0.0001, 4, 1)
