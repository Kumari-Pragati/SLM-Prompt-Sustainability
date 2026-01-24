import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_positive_radius(self):
        """Test surface area calculation for positive radius"""
        radius = 3.14
        expected_result = 12.566368656405024
        self.assertAlmostEqual(surfacearea_sphere(radius), expected_result)

    def test_zero_radius(self):
        """Test surface area calculation for zero radius"""
        radius = 0
        expected_result = 0
        self.assertEqual(surfacearea_sphere(radius), expected_result)

    def test_negative_radius(self):
        """Test surface area calculation for negative radius"""
        radius = -1.73
        with self.assertRaises(ValueError):
            surfacearea_sphere(radius)

    def test_non_numeric_radius(self):
        """Test surface area calculation for non-numeric radius"""
        radius = 'abc'
        with self.assertRaises(TypeError):
            surfacearea_sphere(radius)
