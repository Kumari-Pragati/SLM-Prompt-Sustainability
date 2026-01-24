import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_positive_radius_and_height(self):
        self.assertEqual(surfacearea_cylinder(2, 3), 138.62943)

    def test_zero_radius_and_height(self):
        self.assertEqual(surfacearea_cylinder(0, 0), 0)

    def test_negative_radius_and_positive_height(self):
        self.assertEqual(surfacearea_cylinder(-2, 3), 138.62943)

    def test_positive_radius_and_negative_height(self):
        self.assertEqual(surfacearea_cylinder(2, -3), 138.62943)

    def test_negative_radius_and_negative_height(self):
        self.assertEqual(surfacearea_cylinder(-2, -3), 138.62943)

    def test_invalid_input_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-1, 3)

    def test_invalid_input_zero_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(0, 3)
