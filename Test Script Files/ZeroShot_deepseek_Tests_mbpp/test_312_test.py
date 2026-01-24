import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_volume_cone_positive_values(self):
        self.assertAlmostEqual(volume_cone(3, 4), 37.6991, places=4)
        self.assertAlmostEqual(volume_cone(5, 10), 196.3495, places=4)

    def test_volume_cone_zero_radius(self):
        self.assertEqual(volume_cone(0, 10), 0)

    def test_volume_cone_zero_height(self):
        self.assertEqual(volume_cone(5, 0), 0)

    def test_volume_cone_negative_values(self):
        self.assertRaises(ValueError, volume_cone, -3, 4)
        self.assertRaises(ValueError, volume_cone, 3, -4)
        self.assertRaises(ValueError, volume_cone, -3, -4)
