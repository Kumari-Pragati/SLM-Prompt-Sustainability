import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(parabola_vertex(1, 2, 3), (-1, -1))

    def test_zero_coefficient(self):
        self.assertAlmostEqual(parabola_vertex(0, 0, 0), (0, 0))

    def test_negative_coefficient(self):
        self.assertAlmostEqual(parabola_vertex(-1, -2, -3), (-1, -1))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            parabola_vertex('a', 'b', 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(ZeroDivisionError):
            parabola_vertex(0, 0, 0)
