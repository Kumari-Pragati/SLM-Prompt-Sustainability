import unittest
from mbpp_590_code import polar_rect
import cmath

class TestPolarRect(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1+1j)))

    def test_zero_case(self):
        self.assertEqual(polar_rect(0, 0), ((0, 0), (0+0j)))

    def test_negative_real_case(self):
        self.assertEqual(polar_rect(-1, 1), ((1.4142135623730951, 2.356194490192345), (-1+1j)))

    def test_negative_imaginary_case(self):
        self.assertEqual(polar_rect(1, -1), ((1.4142135623730951, -0.7853981633974483), (1-1j)))

    def test_large_numbers_case(self):
        self.assertEqual(polar_rect(1000, 1000), ((1414.213562373095, 1.1071487177940904), (1000+1000j)))

    def test_pi_case(self):
        self.assertEqual(polar_rect(0, cmath.pi), ((0, 1.5707963267948966), (0+1j)))

    def test_negative_pi_case(self):
        self.assertEqual(polar_rect(0, -cmath.pi), ((0, -1.5707963267948966), (0-1j)))

    def test_nan_case(self):
        with self.assertRaises(TypeError):
            polar_rect(float('nan'), 1)

    def test_inf_case(self):
        with self.assertRaises(TypeError):
            polar_rect(float('inf'), 1)
