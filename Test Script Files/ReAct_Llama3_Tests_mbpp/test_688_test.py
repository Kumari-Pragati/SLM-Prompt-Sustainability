import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):
    def test_positive_real(self):
        self.assertEqual(len_complex(5, 0), 5)

    def test_negative_real(self):
        self.assertEqual(len_complex(-5, 0), 5)

    def test_positive_imaginary(self):
        self.assertEqual(len_complex(0, 5), 5)

    def test_negative_imaginary(self):
        self.assertEqual(len_complex(0, -5), 5)

    def test_zero_real(self):
        self.assertEqual(len_complex(0, 5), 5)

    def test_zero_imaginary(self):
        self.assertEqual(len_complex(5, 0), 5)

    def test_zero_both(self):
        self.assertEqual(len_complex(0, 0), 0)

    def test_non_zero_real(self):
        self.assertEqual(len_complex(5, 5), 7.0710678118654755)

    def test_non_zero_imaginary(self):
        self.assertEqual(len_complex(5, -5), 7.0710678118654755)

    def test_non_zero_real_and_imaginary(self):
        self.assertEqual(len_complex(5, 5), 7.0710678118654755)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            len_complex('a', 5)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            len_complex(5, 'a')
