import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_positive_real(self):
        self.assertEqual(len_complex(1, 0), 1)

    def test_negative_real(self):
        self.assertEqual(len_complex(-1, 0), 1)

    def test_positive_imaginary(self):
        self.assertEqual(len_complex(0, 1), 1)

    def test_negative_imaginary(self):
        self.assertEqual(len_complex(0, -1), 1)

    def test_zero_real(self):
        self.assertEqual(len_complex(0, 1), 1)

    def test_zero_imaginary(self):
        self.assertEqual(len_complex(1, 0), 1)

    def test_zero_real_and_imaginary(self):
        self.assertEqual(len_complex(0, 0), 0)

    def test_non_integer_real(self):
        self.assertAlmostEqual(len_complex(1.5, 0), 1.5)

    def test_non_integer_imaginary(self):
        self.assertAlmostEqual(len_complex(0, 1.5), 1.5)
