import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):
    def test_positive_real_number(self):
        self.assertAlmostEqual(convert(3), cmath.rect(3, 0))

    def test_negative_real_number(self):
        self.assertAlmostEqual(convert(-3), cmath.rect(-3, 0))

    def test_positive_imaginary_number(self):
        self.assertAlmostEqual(convert(0 + 3j), cmath.rect(0, 3))

    def test_negative_imaginary_number(self):
        self.assertAlmostEqual(convert(0 - 3j), cmath.rect(0, -3))

    def test_zero(self):
        self.assertAlmostEqual(convert(0), cmath.rect(0, 0))

    def test_large_positive_real_number(self):
        self.assertAlmostEqual(convert(1e10), cmath.rect(1e10, 0))

    def test_large_negative_real_number(self):
        self.assertAlmostEqual(convert(-1e10), cmath.rect(-1e10, 0))
