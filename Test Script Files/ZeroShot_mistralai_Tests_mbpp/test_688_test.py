import unittest
from mbpp_688_code import len_complex
import cmath

class TestLenComplex(unittest.TestCase):

    def test_zero_complex(self):
        self.assertEqual(len_complex(0, 0), 0)

    def test_positive_complex(self):
        self.assertAlmostEqual(len_complex(1, 1), cmath.sqrt(2))

    def test_negative_complex(self):
        self.assertAlmostEqual(len_complex(-1, -1), cmath.sqrt(2))

    def test_complex_with_zero_real(self):
        self.assertAlmostEqual(len_complex(0, 3), 3)

    def test_complex_with_large_real(self):
        self.assertAlmostEqual(len_complex(1000, 1000), cmath.sqrt(2000000 + 2000000j)**2)

    def test_complex_with_large_imaginary(self):
        self.assertAlmostEqual(len_complex(1, 1000000), cmath.sqrt(1 + 10000000000000j)**2)
