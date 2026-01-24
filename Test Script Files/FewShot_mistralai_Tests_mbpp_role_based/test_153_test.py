import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_positive_a_b_c(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 3), (0.5, 5.5))

    def test_zero_a_b_c(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (0, 0))

    def test_negative_a_b_c(self):
        self.assertAlmostEqual(parabola_vertex(-1, -2, -3), (-0.5, -5.5))

    def test_zero_a(self):
        with self.assertRaises(ValueError):
            parabola_vertex(0, 2, 3)

    def test_zero_b(self):
        with self.assertRaises(ValueError):
            parabola_vertex(1, 0, 3)

    def test_zero_c(self):
        with self.assertRaises(ValueError):
            parabola_vertex(1, 2, 0)
