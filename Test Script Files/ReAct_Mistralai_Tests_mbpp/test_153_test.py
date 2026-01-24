import unittest
from mbpp_153_code import parabola_vertex

class TestParabolaVertex(unittest.TestCase):

    def test_positive_numbers(self):
        "Checks if the function works correctly with positive numbers"
        self.assertAlmostEqual(parabola_vertex(1, 4, 16), (0, 4))
        self.assertAlmostEqual(parabola_vertex(2, 8, 32), (-2, 2))

    def test_zero_coefficients(self):
        "Checks if the function handles zero coefficients correctly"
        self.assertIsNone(parabola_vertex(0, 0, 0))
        self.assertIsNone(parabola_vertex(0, 0, 1))
        self.assertIsNone(parabola_vertex(1, 0, 0))

    def test_negative_numbers(self):
        "Checks if the function works correctly with negative numbers"
        self.assertAlmostEqual(parabola_vertex(-1, -4, 16), (0, 4))
        self.assertAlmostEqual(parabola_vertex(-2, -8, -32), (-2, 2))

    def test_zero_discriminant(self):
        "Checks if the function handles zero discriminant correctly"
        self.assertIsNone(parabola_vertex(1, 2, 2))
        self.assertIsNone(parabola_vertex(1, 2, -2))

    def test_invalid_input(self):
        "Checks if the function raises ValueError for invalid inputs"
        with self.assertRaises(ValueError):
            parabola_vertex(0, 0, 0, 'invalid')
        with self.assertRaises(ValueError):
            parabola_vertex(1, 0, 0, 'invalid')
        with self.assertRaises(ValueError):
            parabola_vertex(0, 1, 0, 'invalid')
