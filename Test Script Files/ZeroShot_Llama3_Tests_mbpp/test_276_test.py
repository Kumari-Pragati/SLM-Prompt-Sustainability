import unittest
from mbpp_276_code import volume_cylinder

class TestVolumeCylinder(unittest.TestCase):

    def test_volume_cylinder(self):
        self.assertAlmostEqual(volume_cylinder(1,2), 6.283, places=3)
        self.assertAlmostEqual(volume_cylinder(2,3), 12.566, places=3)
        self.assertAlmostEqual(volume_cylinder(3,4), 37.699, places=3)
        self.assertAlmostEqual(volume_cylinder(4,5), 113.097, places=3)
        self.assertAlmostEqual(volume_cylinder(5,6), 188.395, places=3)

    def test_volume_cylinder_zero_radius(self):
        self.assertEqual(volume_cylinder(0,2), 0)

    def test_volume_cylinder_zero_height(self):
        self.assertEqual(volume_cylinder(1,0), 0)

    def test_volume_cylinder_negative_radius(self):
        with self.assertRaises(TypeError):
            volume_cylinder(-1,2)

    def test_volume_cylinder_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cylinder(1,-2)
