import unittest
from mbpp_85_code import pi
from your_module import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_sphere(-1)

    def test_valid_radius(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 4 * pi)
        self.assertAlmostEqual(surfacearea_sphere(2), 12.566370614359172)
        self.assertAlmostEqual(surfacearea_sphere(3), 50.26548245743564)
