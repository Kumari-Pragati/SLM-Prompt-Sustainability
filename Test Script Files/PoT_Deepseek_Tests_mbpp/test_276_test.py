import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cylinder(5, 10), 785.375, places=3)

    def test_zero_radius(self):
        self.assertEqual(volume_cylinder(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cylinder(5, 0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cylinder(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cylinder(5, -10)

    def test_large_numbers(self):
        self.assertAlmostEqual(volume_cylinder(1000, 2000), 12566370614.359375, places=3)
