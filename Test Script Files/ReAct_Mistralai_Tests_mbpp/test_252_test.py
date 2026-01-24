import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):

    def test_positive_real_number(self):
        self.assertAlmostEqual(convert(5), cmath.rect(r=5, theta=0))

    def test_negative_real_number(self):
        self.assertAlmostEqual(convert(-5), cmath.rect(r=5, theta=180))

    def test_positive_imaginary_number(self):
        self.assertAlmostEqual(convert(0 + 5j), cmath.rect(r=0, theta=90))

    def test_negative_imaginary_number(self):
        self.assertAlmostEqual(convert(0 - 5j), cmath.rect(r=0, theta=270))

    def test_zero(self):
        self.assertAlmostEqual(convert(0), cmath.rect(r=0, theta=0))

    def test_boundary_cases(self):
        self.assertAlmostEqual(convert(1e-6), cmath.rect(r=1e-6, theta=0))
        self.assertAlmostEqual(convert(1e6), cmath.rect(r=1e6, theta=0))
        self.assertAlmostEqual(convert(complex('inf')), cmath.rect(r=inf, theta=0))
        self.assertAlmostEqual(convert(complex('-inf')), cmath.rect(r=-inf, theta=0))
