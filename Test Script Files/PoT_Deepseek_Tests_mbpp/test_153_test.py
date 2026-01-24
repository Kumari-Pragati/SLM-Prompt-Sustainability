import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_vertex(1, -3, 2), (1.5, 1.25))

    def test_negative_coefficients(self):
        self.assertEqual(parabola_vertex(-1, 3, -2), (-1.5, -1.25))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 1, 1)

    def test_large_numbers(self):
        self.assertEqual(parabola_vertex(1000, -3000, 2000), (1.5, 1.25))

    def test_small_numbers(self):
        self.assertEqual(parabola_vertex(0.001, -0.003, 0.002), (1500.0, 1250.0))

    def test_negative_c(self):
        self.assertEqual(parabola_vertex(1, -3, -2), (1.5, -1.25))
