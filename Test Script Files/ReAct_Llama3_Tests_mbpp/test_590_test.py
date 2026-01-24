import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(polar_rect(1, 2), (cmath.rect(1, 2), cmath.rect(2, cmath.pi)))

    def test_zero_angle(self):
        self.assertEqual(polar_rect(0, 0), (cmath.rect(0, 0), cmath.rect(0, cmath.pi)))

    def test_negative_angle(self):
        self.assertEqual(polar_rect(1, -2), (cmath.rect(1, -2), cmath.rect(2, cmath.pi)))

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            polar_rect(0, 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            polar_rect(-1, 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            polar_rect('a', 2)
