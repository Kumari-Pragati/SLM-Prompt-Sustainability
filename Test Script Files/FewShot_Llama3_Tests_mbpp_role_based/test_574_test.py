import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 392.708)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(surfacearea_cylinder(5, 0), 2 * 3.1415 * 5 * 5)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, -10)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('five', 10)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, 'ten')
