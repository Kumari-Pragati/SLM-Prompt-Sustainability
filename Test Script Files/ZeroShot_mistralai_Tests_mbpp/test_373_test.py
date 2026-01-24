import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_volume_cuboid_positive(self):
        self.assertEqual(volume_cuboid(1, 2, 3), 6)
        self.assertEqual(volume_cuboid(4, 5, 6), 120)
        self.assertEqual(volume_cuboid(7, 8, 9), 531)

    def test_volume_cuboid_zero(self):
        self.assertEqual(volume_cuboid(0, 2, 3), 0)
        self.assertEqual(volume_cuboid(1, 0, 3), 0)
        self.assertEqual(volume_cuboid(1, 2, 0), 0)

    def test_volume_cuboid_negative(self):
        self.assertEqual(volume_cuboid(-1, 2, 3), -6)
        self.assertEqual(volume_cuboid(1, -2, 3), -6)
        self.assertEqual(volume_cuboid(1, 2, -3), -6)
