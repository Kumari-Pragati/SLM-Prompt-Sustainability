import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(parabola_vertex(1, -3, 2), (1.5, 1.25))

    def test_zero_a(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, -3, 2)

    def test_negative_a(self):
        self.assertEqual(parabola_vertex(-1, -3, 2), (1.5, 1.25))

    def test_large_numbers(self):
        self.assertEqual(parabola_vertex(1000000, -3000000, 2000000), (0.0000015, 0.00000125))

    def test_small_numbers(self):
        self.assertEqual(parabola_vertex(0.000001, -0.000003, 0.000002), (1500000.0, 1250000.0))

    def test_negative_c(self):
        self.assertEqual(parabola_vertex(1, -3, -2), (1.5, -1.25))
