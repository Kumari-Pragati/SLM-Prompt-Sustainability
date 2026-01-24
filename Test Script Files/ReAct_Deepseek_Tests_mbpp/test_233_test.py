import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLatersurfaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10, places=2)

    def test_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            lateralsuface_cylinder(5, -10)

    def test_large_numbers(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10000, 20000), 31415000000, places=2)
