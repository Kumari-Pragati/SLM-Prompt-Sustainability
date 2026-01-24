import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483, places=5)

    def test_zero_case(self):
        self.assertEqual(angle_complex(0, 0), 0)

    def test_negative_real_case(self):
        self.assertAlmostEqual(angle_complex(-1, 1), 2.356194490192345, places=5)

    def test_negative_imaginary_case(self):
        self.assertAlmostEqual(angle_complex(1, -1), -0.7853981633974483, places=5)

    def test_large_numbers_case(self):
        self.assertAlmostEqual(angle_complex(1000, 1000), 1.1071487177940904, places=5)

    def test_large_negative_numbers_case(self):
        self.assertAlmostEqual(angle_complex(-1000, 1000), 2.0344439357957027, places=5)

    def test_large_imaginary_numbers_case(self):
        self.assertAlmostEqual(angle_complex(1000, -1000), -1.1071487177940904, places=5)

    def test_large_negative_imaginary_numbers_case(self):
        self.assertAlmostEqual(angle_complex(-1000, -1000), -2.0344439357957027, places=5)

    def test_error_case(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 1)
