import unittest
from mbpp_574_code import surfacearea_cylinder

class TestSurfaceAreaCylinder(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(surfacearea_cylinder(1, 2), 25.13274122471774)
        self.assertEqual(surfacearea_cylinder(3, 4), 157.07963267948964)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(surfacearea_cylinder(0, 1), 6.283185307179586)
        self.assertEqual(surfacearea_cylinder(1, 0), 6.283185307179586)
        self.assertEqual(surfacearea_cylinder(1, float('inf')), 18.849555921538723)
        self.assertEqual(surfacearea_cylinder(float('inf'), 1), 18.849555921538723)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, surfacearea_cylinder, -1, 2)
        self.assertRaises(ValueError, surfacearea_cylinder, 1, -2)
