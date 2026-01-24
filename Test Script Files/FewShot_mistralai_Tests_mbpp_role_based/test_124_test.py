import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_positive_real_and_imaginary(self):
        self.assertAlmostEqual(angle_complex(3, 4), 1.0471975511965979)

    def test_zero_real_and_imaginary(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0)

    def test_negative_real_and_positive_imaginary(self):
        self.assertAlmostEqual(angle_complex(-3, 4), 2.094395102393195)

    def test_negative_real_and_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(-3, -4), 3.141592653589793)

    def test_large_positive_real_and_imaginary(self):
        self.assertAlmostEqual(angle_complex(1e6, 1e6), 1.5707963267948966)

    def test_large_negative_real_and_imaginary(self):
        self.assertAlmostEqual(angle_complex(-1e6, -1e6), -1.5707963267948966)

    def test_complex_conjugate(self):
        self.assertAlmostEqual(angle_complex(3, 4), angle_complex(-3, -4))
