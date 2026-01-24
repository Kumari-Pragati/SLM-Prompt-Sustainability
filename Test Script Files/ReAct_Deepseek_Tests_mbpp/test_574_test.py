import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(2, 5), 62.83*2 + 62.83*10)

    def test_zero_radius(self):
        self.assertEqual(surfacearea_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(surfacearea_cylinder(2, 0), 2*3.1415*2*0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-2, 5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surfacearea_cylinder(2, -5)

    def test_large_numbers(self):
        self.assertAlmostEqual(surfacearea_cylinder(1000, 2000), 6283000)
