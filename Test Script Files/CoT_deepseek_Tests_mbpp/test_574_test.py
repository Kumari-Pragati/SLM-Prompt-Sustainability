import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 314.15*12, places=2)

    def test_small_radius(self):
        self.assertAlmostEqual(surfacearea_cylinder(0.1, 10), 3.1415*2*0.1*0.1 + 3.1415*2*0.1*10, places=2)

    def test_large_radius(self):
        self.assertAlmostEqual(surfacearea_cylinder(1000, 10), 3.1415*2*1000*1000 + 3.1415*2*1000*10, places=2)

    def test_small_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 0.1), 3.1415*2*5*5 + 3.1415*2*5*0.1, places=2)

    def test_large_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 1000), 3.1415*2*5*5 + 3.1415*2*5*1000, places=2)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(surfacearea_cylinder(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(5, -10)
