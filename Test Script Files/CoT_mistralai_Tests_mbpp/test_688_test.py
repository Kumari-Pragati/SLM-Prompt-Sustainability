import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_positive_real_and_imaginary(self):
        self.assertEqual(len_complex(3, 4), 5)

    def test_zero_complex(self):
        self.assertEqual(len_complex(0, 0), 0)

    def test_negative_real_and_imaginary(self):
        self.assertEqual(len_complex(-3, -4), 5)

    def test_large_complex(self):
        self.assertAlmostEqual(len_complex(1e10, 1e10), 1.4142135623730951e11)

    def test_complex_with_zero_imaginary(self):
        self.assertEqual(len_complex(3, 0), 3)

    def test_complex_with_zero_real(self):
        self.assertEqual(len_complex(0, 3j), 3)

    def test_invalid_input_real(self):
        with self.assertRaises(ValueError):
            len_complex('a', b=0)

    def test_invalid_input_imaginary(self):
        with self.assertRaises(ValueError):
            len_complex(a=0, 'b')
