import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):
    def test_valid_positive_values(self):
        self.assertAlmostEqual(volume_cone(1, 2), 6.283185307179586)
        self.assertAlmostEqual(volume_cone(2, 3), 33.50094595322402)

    def test_zero_radius(self):
        self.assertAlmostEqual(volume_cone(0, 1), 0.0)

    def test_zero_height(self):
        self.assertAlmostEqual(volume_cone(1, 0), 0.0)

    def test_negative_radius(self):
        self.assertRaises(ValueError, volume_cone, -1, 1)

    def test_negative_height(self):
        self.assertRaises(ValueError, volume_cone, 1, -1)
