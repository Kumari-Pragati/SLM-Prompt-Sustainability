import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_simple_cylinder(self):
        self.assertEqual(surfacearea_cylinder(1, 2), 25.132741224717773)
        self.assertEqual(surfacearea_cylinder(2, 3), 113.0976280347353)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cylinder(0, 1), 6.283185307179586)
        self.assertEqual(surfacearea_cylinder(1, 0), 6.283185307179586)
        self.assertEqual(surfacearea_cylinder(1, 0), 6.283185307179586)

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cylinder(1e-5, 1e5), 62831853.07179586)
        self.assertEqual(surfacearea_cylinder(1e5, 1e-5), 62831853.07179586)
