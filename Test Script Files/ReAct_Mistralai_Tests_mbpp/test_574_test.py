import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(surfacearea_cylinder(1, 2), 25.132741224717773)
        self.assertEqual(surfacearea_cylinder(3, 4), 167.73940254649674)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(0, 5)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(2, 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-1, 2)
        with self.assertRaises(ValueError):
            surfacearea_cylinder(2, -3)

    def test_float_and_int_values(self):
        self.assertEqual(surfacearea_cylinder(1.5, 2), 28.274333882308138)
        self.assertEqual(surfacearea_cylinder(2, 3), 75.3982207166359)
