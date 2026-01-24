import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 314.15*2 + 314.15*10*2)

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 314.15*2)

    def test_negative_radius(self):
        with self.assertRaises(Exception):
            surfacearea_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(Exception):
            surfacearea_cylinder(5, -10)

    def test_large_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(1000, 2000), 314.15*2*1000*2 + 314.15*2000*2)
