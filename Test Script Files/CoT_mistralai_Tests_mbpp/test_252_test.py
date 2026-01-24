import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):
    def test_positive_real_number(self):
        self.assertAlmostEqual(convert(5), cmath.rect(r=5, theta=0))

    def test_positive_imaginary_number(self):
        self.assertAlmostEqual(convert(5j), cmath.rect(r=0, theta=1.5707963267948966))

    def test_complex_number(self):
        self.assertAlmostEqual(convert(3+4j), cmath.rect(r=5, theta=0.6435011087932847))

    def test_zero(self):
        self.assertAlmostEqual(convert(0), cmath.rect(r=0, theta=0))

    def test_negative_real_number(self):
        self.assertAlmostEqual(convert(-5), cmath.rect(r=5, theta=3.141592653589793))

    def test_negative_imaginary_number(self):
        self.assertAlmostEqual(convert(-5j), cmath.rect(r=0, theta=-1.5707963267948966))

    def test_invalid_input(self):
        self.assertRaises(TypeError, convert, "string")
