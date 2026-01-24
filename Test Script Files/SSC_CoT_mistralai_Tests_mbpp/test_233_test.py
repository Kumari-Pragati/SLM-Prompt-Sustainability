import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.566368071386508)
        self.assertEqual(lateralsuface_cylinder(3, 4), 50.26548245743669)

    def test_edge_input(self):
        self.assertEqual(lateralsuface_cylinder(0, 1), 0)
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_boundary_input(self):
        self.assertEqual(lateralsuface_cylinder(1e-5, 1), 3.141592653589793)
        self.assertEqual(lateralsuface_cylinder(1, 1e-5), 3.141592653589793)

    def test_negative_input(self):
        self.assertEqual(lateralsuface_cylinder(-1, 2), -6.283185307179586)
        self.assertEqual(lateralsuface_cylinder(1, -2), -12.566368071386508)
