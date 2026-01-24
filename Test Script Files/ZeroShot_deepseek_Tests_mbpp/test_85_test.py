import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_positive_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359172)
        self.assertAlmostEqual(surfacearea_sphere(2), 50.26544290927258)
        self.assertAlmostEqual(surfacearea_sphere(3), 113.09733552923254)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)
