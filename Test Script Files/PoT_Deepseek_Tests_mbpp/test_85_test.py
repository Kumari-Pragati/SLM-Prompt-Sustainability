import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359172)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1000), 125663.70614359172)

    def test_float_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(2.5), 78.53981633759773)
