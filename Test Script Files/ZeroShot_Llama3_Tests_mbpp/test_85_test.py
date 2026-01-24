import unittest
from mbpp_85_code import surfacearea_sphere

class TestSurfaceAreaSphere(unittest.TestCase):

    def test_surface_area_sphere(self):
        self.assertAlmostEqual(surfacearea_sphere(1), 12.566370614359272)
        self.assertAlmostEqual(surfacearea_sphere(2), 50.26548245743669)
        self.assertAlmostEqual(surfacearea_sphere(3), 113.09733552923253)
        self.assertAlmostEqual(surfacearea_sphere(4), 201.06192982974676)
        self.assertAlmostEqual(surfacearea_sphere(5), 314.1592653589793)

    def test_surface_area_sphere_zero(self):
        self.assertEqual(surfacearea_sphere(0), 0)

    def test_surface_area_sphere_negative(self):
        with self.assertRaises(TypeError):
            surfacearea_sphere(-1)
