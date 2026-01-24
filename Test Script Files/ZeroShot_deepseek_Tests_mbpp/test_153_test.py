import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_positive_a(self):
        self.assertEqual(parabola_vertex(1, -3, 2), (1.5, 2.25))

    def test_negative_a(self):
        self.assertEqual(parabola_vertex(-1, 3, -2), (-1.5, -2.25))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 1, 1)

    def test_negative_b(self):
        self.assertEqual(parabola_vertex(1, -2, 1), (1, 1))

    def test_zero_b(self):
        self.assertEqual(parabola_vertex(1, 0, 1), (0, 1))

    def test_negative_c(self):
        self.assertEqual(parabola_vertex(1, 1, -2), (0.5, -0.25))

    def test_zero_c(self):
        self.assertEqual(parabola_vertex(1, 1, 0), (0.5, 0))
