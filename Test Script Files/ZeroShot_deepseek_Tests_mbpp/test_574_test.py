import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(1, 1), 12.566, places=3)
        self.assertAlmostEqual(surfacearea_cylinder(2, 3), 62.832, places=3)
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 314.150, places=3)

    def test_zero_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0)
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 0)
        self.assertAlmostEqual(surfacearea_cylinder(10, 0), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(surfacearea_cylinder(-1, -1), 12.566, places=3)
        self.assertAlmostEqual(surfacearea_cylinder(-2, -3), 62.832, places=3)
        self.assertAlmostEqual(surfacearea_cylinder(-5, -10), 314.150, places=3)

    def test_invalid_values(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder("1", 1)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(1, "1")
        with self.assertRaises(TypeError):
            surfacearea_cylinder("1", "1")
