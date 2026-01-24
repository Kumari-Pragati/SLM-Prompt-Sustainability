import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_cylinder(2, 3), 15.707963267948966)

    def test_edge_case_zero_radius(self):
        self.assertEqual(surfacearea_cylinder(0, 3), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(surfacearea_cylinder(2, 0), 12.566370614359172)

    def test_corner_case_negative_radius(self):
        self.assertEqual(surfacearea_cylinder(-1, 3), -6.283185307179586)

    def test_corner_case_negative_height(self):
        self.assertEqual(surfacearea_cylinder(2, -1), -6.283185307179586)
