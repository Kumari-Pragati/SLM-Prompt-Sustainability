import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cylinder(2, 5), 62.83*4, places=2)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 0, places=2)
        self.assertAlmostEqual(surfacearea_cylinder(1, 0), 2*3.1415, places=2)

    def test_corner_cases(self):
        self.assertAlmostEqual(surfacearea_cylinder(0.5, 20), 31.415*4, places=2)
        self.assertAlmostEqual(surfacearea_cylinder(100, 1), 6283.0*2, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder("2", 5)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(2, "5")
        with self.assertRaises(ValueError):
            surfacearea_cylinder(-2, 5)
        with self.assertRaises(ValueError):
            surfacearea_cylinder(2, -5)
