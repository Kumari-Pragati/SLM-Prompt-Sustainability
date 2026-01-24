import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.56637061435927)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere(-1)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere('a')
