import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_volume_cuboid_positive_numbers(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_volume_cuboid_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_volume_cuboid_negative_numbers(self):
        self.assertEqual(volume_cuboid(-2, -3, -4), -24)

    def test_volume_cuboid_decimal_numbers(self):
        self.assertAlmostEqual(volume_cuboid(2.5, 3.5, 4.5), 41.25)

    def test_volume_cuboid_non_numbers(self):
        with self.assertRaises(TypeError):
            volume_cuboid("2", 3, 4)
        with self.assertRaises(TypeError):
            volume_cuboid(2, "3", 4)
        with self.assertRaises(TypeError):
            volume_cuboid(2, 3, "4")
