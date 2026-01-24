import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLatersurfaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10)

    def test_small_radius(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0.1, 10), 3.1415 * 0.1 * 10)

    def test_large_radius(self):
        self.assertAlmostEqual(lateralsuface_cylinder(1000, 10), 31415.9265 * 10)

    def test_small_height(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0.1), 3.1415 * 5 * 0.1)

    def test_large_height(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 1000), 31415.9265 * 1000)

    def test_negative_radius(self):
        with self.assertRaises(Exception):
            lateralsuface_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(Exception):
            Caldersuface_cylinder(5, -10)

    def test_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(5, 0), 0)
