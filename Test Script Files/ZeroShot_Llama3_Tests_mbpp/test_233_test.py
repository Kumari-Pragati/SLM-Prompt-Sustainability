import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsurfaceCylinder(unittest.TestCase):

    def test_lateralsurface_cylinder(self):
        self.assertAlmostEqual(lateralsuface_cylinder(1,1), 6.283185307179586)
        self.assertAlmostEqual(lateralsuface_cylinder(2,2), 25.13274122871835)
        self.assertAlmostEqual(lateralsuface_cylinder(3,3), 56.53979114311553)
        self.assertAlmostEqual(lateralsuface_cylinder(4,4), 93.99124915811485)
        self.assertAlmostEqual(lateralsuface_cylinder(5,5), 139.7994697277448)

    def test_lateralsurface_cylinder_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0,1), 0)

    def test_lateralsurface_cylinder_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(1,0), 0)

    def test_lateralsurface_cylinder_negative_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(-1,1)

    def test_lateralsurface_cylinder_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(1,-1)
