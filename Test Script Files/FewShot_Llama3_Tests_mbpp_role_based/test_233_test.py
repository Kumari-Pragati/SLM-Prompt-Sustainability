import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsurfaceCylinder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 628.32)

    def test_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, -10)
