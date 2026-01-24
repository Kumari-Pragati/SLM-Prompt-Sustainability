import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359172, places=5)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(100), 1256.6370614359173, places=5)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)
