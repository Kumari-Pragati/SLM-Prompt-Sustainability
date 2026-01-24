import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_len_complex_positive(self):
        self.assertAlmostEqual(len_complex(3, 4), 5.0)

    def test_len_complex_negative(self):
        self.assertAlmostEqual(len_complex(-3, -4), 5.0)

    def test_len_complex_zero(self):
        self.assertAlmostEqual(len_complex(0, 0), 0.0)

    def test_len_complex_real_zero(self):
        self.assertAlmostEqual(len_complex(0, 4), 4.0)

    def test_len_complex_imag_zero(self):
        self.assertAlmostEqual(len_complex(3, 0), 3.0)

    def test_len_complex_large_numbers(self):
        self.assertAlmostEqual(len_complex(1000, 2000), 2236.0683668600285)
