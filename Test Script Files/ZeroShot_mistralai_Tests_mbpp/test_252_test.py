import unittest
from mbpp_252_code import polar

class TestConvertFunction(unittest.TestCase):

    def test_convert_positive_real_number(self):
        self.assertAlmostEqual(convert(1), polar(1, 0))

    def test_convert_negative_real_number(self):
        self.assertAlmostEqual(convert(-1), polar(-1, 0))

    def test_convert_positive_imaginary_number(self):
        self.assertAlmostEqual(convert(1j), polar(0, 1))

    def test_convert_negative_imaginary_number(self):
        self.assertAlmostEqual(convert(-1j), polar(0, -1))

    def test_convert_complex_number_with_magnitude_and_angle(self):
        self.assertAlmostEqual(convert(2 + 3j), polar(5, cmath.pi/4))
