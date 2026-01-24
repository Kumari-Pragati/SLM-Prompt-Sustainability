import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLatersurfaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 314.15 * 10 * 2, msg="Typical case failed")

    def test_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(5, 0), 0, msg="Zero height failed")

    def test_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 10), 0, msg="Zero radius failed")

    def test_negative_height(self):
        with self.assertRaises(Exception, msg="Negative height not handled"):
            lateralsuface_cylinder(5, -10)

    def test_negative_radius(self):
        with self.assertRaises(Exception, msg="Negative radius not handled"):
            lateralsuface_cylinder(-5, 10)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception, msg="Non-numeric input not handled"):
            lateralsuface_cylinder("five", 10)
