import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_surface_area_of_cylinder_with_valid_input(self):
        self.assertEqual(surfacearea_cylinder(1, 2), 15.707963267948966)
        self.assertEqual(surfacearea_cylinder(2, 3), 70.68558807749973)
        self.assertEqual(surfacearea_cylinder(3, 4), 264.9938912207185)

    def test_surface_area_of_cylinder_with_zero_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(0, 1)

    def test_surface_area_of_cylinder_with_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-1, 1)

    def test_surface_area_of_cylinder_with_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(1, -1)
