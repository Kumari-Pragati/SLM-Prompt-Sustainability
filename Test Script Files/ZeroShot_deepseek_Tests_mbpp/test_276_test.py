import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_volume_cylinder_positive_values(self):
        self.assertAlmostEqual(volume_cylinder(1, 2), 3.1415, places=4)
        self.assertAlmostEqual(volume_cylinder(2, 3), 62.83, places=2)
        self.assertAlmostEqual(volume_cylinder(5, 10), 785.3975, places=3)

    def test_volume_cylinder_zero_radius(self):
        self.assertEqual(volume_cylinder(0, 10), 0)

    def test_volume_cylinder_zero_height(self):
        self.assertEqual(volume_cylinder(1, 0), 0)

    def test_volume_cylinder_negative_values(self):
        self.assertRaises(ValueError, volume_cylinder, -1, 2)
        self.assertRaises(ValueError, volume_cylinder, 1, -2)
        self.assertRaises(ValueError, volume_cylinder, -1, -2)
