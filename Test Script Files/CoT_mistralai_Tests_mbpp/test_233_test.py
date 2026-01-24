import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.566368071386508)
        self.assertEqual(lateralsuface_cylinder(3, 4), 75.3982208136887)

    def test_zero_value(self):
        self.assertEqual(lateralsuface_cylinder(0, 1), 0)
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_negative_values(self):
        self.assertEqual(lateralsuface_cylinder(-1, 2), -6.283185307179586)
        self.assertEqual(lateralsuface_cylinder(1, -2), -12.566368071386508)

    def test_float_values(self):
        self.assertAlmostEqual(lateralsuface_cylinder(2.5, 3.5), 39.74395698292753)
        self.assertAlmostEqual(lateralsuface_cylinder(3.5, 2.5), 39.74395698292753)
