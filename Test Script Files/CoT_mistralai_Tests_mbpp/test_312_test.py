import unittest
from mbpp_312_code import volume_cone

class TestVolumeCone(unittest.TestCase):
    def test_positive_values(self):
        self.assertAlmostEqual(volume_cone(1, 2), 6.283185307179586)
        self.assertAlmostEqual(volume_cone(2, 3), 33.50094595322402)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            volume_cone(0, 1)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            volume_cone(1, 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            volume_cone(-1, 2)
        with self.assertRaises(ValueError):
            volume_cone(1, -2)
