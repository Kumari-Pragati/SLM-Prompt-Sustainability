import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 392.7083333333333)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 62.83185307179586)
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 78.53981633974483)

    def test_zero_radius(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 62.83185307179586)

    def test_zero_height(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 78.53981633974483)

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
