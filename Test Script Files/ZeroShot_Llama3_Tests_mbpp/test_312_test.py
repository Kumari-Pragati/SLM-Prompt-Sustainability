import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):

    def test_volume_cone_positive(self):
        self.assertAlmostEqual(volume_cone(1, 2), 3.14159265359)

    def test_volume_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            volume_cone(-1, 2)

    def test_volume_cone_negative_height(self):
        with self.assertRaises(ValueError):
            volume_cone(1, -2)

    def test_volume_cone_zero_radius(self):
        self.assertAlmostEqual(volume_cone(0, 2), 0)

    def test_volume_cone_zero_height(self):
        self.assertAlmostEqual(volume_cone(1, 0), 0)

    def test_volume_cone_zero_radius_and_height(self):
        self.assertAlmostEqual(volume_cone(0, 0), 0)
