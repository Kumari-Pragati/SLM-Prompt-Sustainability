import unittest
from mbpp_590_code import polar_rect
import cmath

class TestPolarRect(unittest.TestCase):

    def test_polar_rect(self):
        # Test with positive real and imaginary parts
        self.assertEqual(polar_rect(1, 1), ((1.4142135623730951, 0.7853981633974483), (1+0j)))

        # Test with negative real and positive imaginary parts
        self.assertEqual(polar_rect(-1, 1), ((-1.4142135623730951, 2.356194490192345), (-1+1j)))

        # Test with negative real and negative imaginary parts
        self.assertEqual(polar_rect(-1, -1), ((-1.4142135623730951, -0.7853981633974483), (-1-1j)))

        # Test with positive real and negative imaginary parts
        self.assertEqual(polar_rect(1, -1), ((1.4142135623730951, -2.356194490192345), (1-1j)))

        # Test with zero real part and positive imaginary part
        self.assertEqual(polar_rect(0, 1), ((0, 1.5707963267948966), 0j))

        # Test with zero real part and negative imaginary part
        self.assertEqual(polar_rect(0, -1), ((0, -1.5707963267948966), -1j))

        # Test with zero imaginary part
        self.assertEqual(polar_rect(1, 0), ((1, 0), 1+0j))

        # Test with zero real and imaginary parts
        self.assertEqual(polar_rect(0, 0), ((0, 0), 0j))
