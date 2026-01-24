import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_positive_real_positive_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, 1), cmath.phase(complex(1, 1)))

    def test_negative_real_positive_imaginary(self):
        self.assertAlmostEqual(angle_complex(-1, 1), cmath.phase(complex(-1, 1)))

    def test_positive_real_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, -1), cmath.phase(complex(1, -1)))

    def test_negative_real_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(-1, -1), cmath.phase(complex(-1, -1)))

    def test_zero_real_positive_imaginary(self):
        self.assertAlmostEqual(angle_complex(0, 1), cmath.phase(complex(0, 1)))

    def test_zero_real_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(0, -1), cmath.phase(complex(0, -1)))

    def test_zero_real_zero_imaginary(self):
        self.assertAlmostEqual(angle_complex(0, 0), cmath.phase(complex(0, 0)))

    def test_nonzero_real_nonzero_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, 2), cmath.phase(complex(1, 2)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            angle_complex("a", 1)
