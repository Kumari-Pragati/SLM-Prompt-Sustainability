import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(3), 4 * math.pi * 9)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1e6), 4 * math.pi * 1e12)
