import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralSurfaceCylinder(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(lateralsuface_cylinder(2, 3), 2 * 3.1415 * 2 * 3)

    def test_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 3), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(2, 0), 0)

    def test_negative_values(self):
        self.assertRaises(ValueError, lateralsuface_cylinder, -1, 3)
        self.assertRaises(ValueError, lateralsuface_cylinder, 2, -1)
