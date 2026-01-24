import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):
    def test_positive_real_and_imaginary(self):
        self.assertEqual(polar_rect(3, 4), (cmath.polar(complex(3, 4)), cmath.rect(2, cmath.pi)))

    def test_zero_real_and_imaginary(self):
        self.assertEqual(polar_rect(0, 0), (cmath.polar(complex(0, 0)), cmath.rect(2, cmath.pi)))

    def test_negative_real_and_imaginary(self):
        self.assertEqual(polar_rect(-3, -4), (cmath.polar(complex(-3, -4)), cmath.rect(2, cmath.pi)))

    def test_large_real_and_imaginary(self):
        self.assertEqual(polar_rect(1e6, 1e6), (cmath.polar(complex(1e6, 1e6)), cmath.rect(2, cmath.pi)))

    def test_small_real_and_imaginary(self):
        self.assertEqual(polar_rect(1e-6, 1e-6), (cmath.polar(complex(1e-6, 1e-6)), cmath.rect(2, cmath.pi)))

    def test_nan_input(self):
        with self.assertRaises(ValueError):
            polar_rect(float('nan'), float('nan'))

    def test_inf_input(self):
        with self.assertRaises(ValueError):
            polar_rect(float('inf'), float('inf'))
