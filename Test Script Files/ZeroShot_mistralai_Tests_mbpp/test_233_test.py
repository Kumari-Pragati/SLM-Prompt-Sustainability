import unittest
from mbpp_233_code import pi
from 233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):

    def test_lateral_surface_cylinder_positive(self):
        self.assertAlmostEqual(lateralsuface_cylinder(2, 3), 2 * pi * 6)
        self.assertAlmostEqual(lateralsuface_cylinder(3, 4), 2 * pi * 12)
        self.assertAlmostEqual(lateralsuface_cylinder(4, 5), 2 * pi * 20)

    def test_lateral_surface_cylinder_zero(self):
        self.assertEqual(lateralsuface_cylinder(0, 1), 0)
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_lateral_surface_cylinder_negative(self):
        self.assertAlmostEqual(lateralsuface_cylinder(-2, 3), -2 * pi * 6)
        self.assertAlmostEqual(lateralsuface_cylinder(3, -2), -2 * pi * 6)
