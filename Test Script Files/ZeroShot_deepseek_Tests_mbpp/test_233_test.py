import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLatersurfaceCylinder(unittest.TestCase):

    def test_latersurface_cylinder_positive_values(self):
        self.assertAlmostEqual(latersurface_cylinder(1, 1), 6.283, places=3)
        self.assertAlmostEqual(latersurface_cylinder(2, 3), 37.698, places=3)
        self.assertAlmostEqual(latersurface_cylinder(5, 10), 314.15, places=3)

    def test_latersurface_cylinder_zero_values(self):
        self.assertEqual(latersurface_cylinder(0, 0), 0)
        self.assertEqual(latersurface_cylinder(0, 10), 0)
        self.assertEqual(latersurface_cylinder(10, 0), 0)

    def test_latersurface_cylinder_negative_values(self):
        self.assertRaises(ValueError, lateralsuface_cylinder, -1, 1)
        self.assertRaises(ValueError, lateralsuface_cylinder, 1, -1)
        self.assertRaises(ValueError, lateralsuface_cylinder, -1, -1)
