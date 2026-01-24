import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.566368064502437)
        self.assertEqual(lateralsuface_cylinder(2, 3), 18.849555921538738)

    def test_edge_input(self):
        self.assertEqual(lateralsuface_cylinder(0, 1), 0)
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_boundary_input(self):
        self.assertEqual(lateralsuface_cylinder(1e-5, 1e5), 314159.2653589793)
        self.assertEqual(lateralsuface_cylinder(1e5, 1e-5), 314159.2653589793)
