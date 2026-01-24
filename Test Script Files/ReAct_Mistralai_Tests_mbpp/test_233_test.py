import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.566368071386508)
        self.assertEqual(lateralsuface_cylinder(3, 4), 75.3982208136887)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(0, 1)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(1, 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(-1, 2)
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(1, -2)

    def test_float_and_int_values(self):
        self.assertEqual(lateralsuface_cylinder(2.5, 3), 28.274333882308138)
        self.assertEqual(lateralsuface_cylinder(3, 2), 28.274333882308138)
