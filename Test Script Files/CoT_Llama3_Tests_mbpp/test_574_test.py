import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertAlmostEqual(surfacearea_cylinder(5, 10), 392.699081, places=5)

    def test_edge_cases(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 10), 62.831853, places=5)
        self.assertAlmostEqual(surfacearea_cylinder(5, 0), 78.539816, places=5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cylinder('a', 10)
        with self.assertRaises(TypeError):
            surfacearea_cylinder(5, 'b')

    def test_boundary_conditions(self):
        self.assertAlmostEqual(surfacearea_cylinder(0, 0), 0, places=5)
        self.assertAlmostEqual(surfacearea_cylinder(float('inf'), float('inf')), float('inf'), places=5)
