import unittest
from mbpp_688_code import len_complex

class TestLenComplex(unittest.TestCase):

    def test_positive_real_and_imaginary(self):
        """Test complex number with positive real and imaginary parts"""
        self.assertEqual(len_complex(3, 4), 5)

    def test_zero_real_and_imaginary(self):
        """Test complex number with zero real and imaginary parts"""
        self.assertEqual(len_complex(0, 0), 0)

    def test_negative_real_and_positive_imaginary(self):
        """Test complex number with negative real and positive imaginary parts"""
        self.assertEqual(len_complex(-3, 4), 5)

    def test_negative_real_and_negative_imaginary(self):
        """Test complex number with negative real and negative imaginary parts"""
        self.assertEqual(len_complex(-3, -4), 5)

    def test_edge_case_zero_real_and_non_zero_imaginary(self):
        """Test complex number with zero real and non-zero imaginary part"""
        self.assertAlmostEqual(len_complex(0.00001, 4), 4.00001)

    def test_edge_case_non_zero_real_and_zero_imaginary(self):
        """Test complex number with non-zero real and zero imaginary part"""
        self.assertAlmostEqual(len_complex(4, 0.00001), 4.00001)

    def test_edge_case_complex_number_with_small_real_and_imaginary(self):
        """Test complex number with small real and imaginary parts"""
        self.assertAlmostEqual(len_complex(0.00001, 0.00001), 0.00002)

    def test_error_case_non_numeric_input(self):
        """Test error case: non-numeric input"""
        with self.assertRaises(TypeError):
            len_complex('a', 'b')
