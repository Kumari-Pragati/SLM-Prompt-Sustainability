import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_volume_cuboid_typical(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_volume_cuboid_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_volume_cuboid_negative(self):
        self.assertEqual(volume_cuboid(-2, 3, 4), -24)

    def test_volume_cuboid_non_numeric(self):
        with self.assertRaises(TypeError):
            volume_cuboid('a', 3, 4)

    def test_volume_cuboid_mixed_types(self):
        with self.assertRaises(TypeError):
            volume_cuboid(2, 'b', 4)

    def test_volume_cuboid_mixed_types2(self):
        with self.assertRaises(TypeError):
            volume_cuboid(2, 3, 'c')
