import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(surfacearea_cylinder(1, 2), 18.8495563274)
        self.assertAlmostEqual(surfacearea_cylinder(2, 3), 38.1887906548)
        self.assertAlmostEqual(surfacearea_cylinder(3, 4), 63.5881562964)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0)
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 60.0)
        self.assertAlmostEqual(surfacearea_cylinder(10, 0), 60.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('a', 2)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(1, 'b')
