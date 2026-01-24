import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsufaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        result = lateralsuface_cylinder(5, 10)
        self.assertAlmostEqual(result, 314.15, places=2)

    def test_zero_radius(self):
        with self.assertRaises(ZeroDivisionError):
            lateralsuface_cylinder(0, 10)

    def test_zero_height(self):
        result = lateralsuface_cylinder(5, 0)
        self.assertEqual(result, 0)

    def test_negative_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, -10)

    def test_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('five', 10)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, 'ten')
