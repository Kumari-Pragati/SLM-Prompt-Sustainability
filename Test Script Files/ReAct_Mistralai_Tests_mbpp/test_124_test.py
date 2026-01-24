import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_positive_real_and_imaginary(self):
        """Test angle for positive real and imaginary numbers"""
        self.assertAlmostEqual(angle_complex(3, 4), 1.0471975511965979, delta=1e-5)

    def test_zero_real_and_imaginary(self):
        """Test angle for zero real and imaginary numbers"""
        self.assertAlmostEqual(angle_complex(0, 0), 0, delta=1e-5)

    def test_negative_real_and_positive_imaginary(self):
        """Test angle for negative real and positive imaginary numbers"""
        self.assertAlmostEqual(angle_complex(-3, 4), 2.0943951023931953, delta=1e-5)

    def test_negative_real_and_negative_imaginary(self):
        """Test angle for negative real and negative imaginary numbers"""
        self.assertAlmostEqual(angle_complex(-3, -4), 3.141592653589793, delta=1e-5)

    def test_edge_case_zero_imaginary(self):
        """Test angle for zero imaginary number"""
        self.assertAlmostEqual(angle_complex(3, 0), 1.5707963267948966, delta=1e-5)

    def test_edge_case_one_imaginary(self):
        """Test angle for one imaginary number"""
        self.assertAlmostEqual(angle_complex(0, 1), 1.5707963267948966, delta=1e-5)

    def test_error_case_non_complex(self):
        """Test error case when input is not a complex number"""
        with self.assertRaises(TypeError):
            angle_complex('abc', 123)
