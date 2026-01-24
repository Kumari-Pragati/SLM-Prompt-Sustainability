import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_positive_real_and_imaginary(self):
        self.assertAlmostEqual(len_complex(3, 4), 5)

    def test_zero_real_and_imaginary(self):
        self.assertAlmostEqual(len_complex(0, 0), 0)

    def test_negative_real_and_positive_imaginary(self):
        self.assertAlmostEqual(len_complex(-3, 4), 5)

    def test_negative_real_and_negative_imaginary(self):
        self.assertAlmostEqual(len_complex(-3, -4), 5)

    def test_complex_with_large_magnitude(self):
        self.assertAlmostEqual(len_complex(1000, 1000), 1414.2135623730951)

    def test_complex_with_small_magnitude(self):
        self.assertAlmostEqual(len_complex(0.001, 0.001), 0.0014142135623730951)

    def test_complex_with_zero_imaginary(self):
        self.assertAlmostEqual(len_complex(3, 0), 3)

    def test_complex_with_zero_real(self):
        self.assertAlmostEqual(len_complex(0, 3), 3)
