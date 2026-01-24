import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_positive_values(self):
        """Test polar_rect with positive x and y values"""
        result = polar_rect(3, 4)
        self.assertAlmostEqual(result[0].real, 3, delta=0.01)
        self.assertAlmostEqual(result[0].imag, 4, delta=0.01)
        self.assertAlmostEqual(result[1].real, 3 * cmath.cos(2 + cmath.pi), delta=0.01)
        self.assertAlmostEqual(result[1].imag, 3 * cmath.sin(2 + cmath.pi), delta=0.01)

    def test_zero_values(self):
        """Test polar_rect with zero x or y values"""
        result1 = polar_rect(0, 4)
        result2 = polar_rect(4, 0)
        self.assertAlmostEqual(result1[0].real, 0, delta=0.01)
        self.assertAlmostEqual(result1[0].imag, 4, delta=0.01)
        self.assertAlmostEqual(result1[1].real, 4 * cmath.cos(2 + cmath.pi), delta=0.01)
        self.assertAlmostEqual(result1[1].imag, 4 * cmath.sin(2 + cmath.pi), delta=0.01)

        self.assertAlmostEqual(result2[0].real, 0, delta=0.01)
        self.assertAlmostEqual(result2[0].imag, 4, delta=0.01)
        self.assertAlmostEqual(result2[1].real, 4 * cmath.cos(2), delta=0.01)
        self.assertAlmostEqual(result2[1].imag, 4 * cmath.sin(2), delta=0.01)

    def test_negative_values(self):
        """Test polar_rect with negative x and y values"""
        result = polar_rect(-3, -4)
        self.assertAlmostEqual(result[0].real, -3, delta=0.01)
        self.assertAlmostEqual(result[0].imag, -4, delta=0.01)
        self.assertAlmostEqual(result[1].real, -3 * cmath.cos(2 + cmath.pi), delta=0.01)
        self.assertAlmostEqual(result[1].imag, -3 * cmath.sin(2 + cmath.pi), delta=0.01)

    def test_complex_input(self):
        """Test polar_rect with complex input"""
        result = polar_rect(2 + 3j, 4 + 5j)
        self.assertAlmostEqual(result[0].real, 2, delta=0.01)
        self.assertAlmostEqual(result[0].imag, 3, delta=0.01)
        self.assertAlmostEqual(result[1].real, (2 * cmath.cos(2 + cmath.pi) + 3 * cmath.sin(2 + cmath.pi)) + 4j, delta=0.01)
        self.assertAlmostEqual(result[1].imag, (-2 * cmath.sin(2 + cmath.pi) + 3 * cmath.cos(2 + cmath.pi)) + 5j, delta=0.01)
