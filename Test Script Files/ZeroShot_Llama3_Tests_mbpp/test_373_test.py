import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_volume_cuboid_positive(self):
        self.assertEqual(volume_cuboid(1,2,3), 6)

    def test_volume_cuboid_negative(self):
        self.assertEqual(volume_cuboid(-1,-2,-3), 6)

    def test_volume_cuboid_zero(self):
        self.assertEqual(volume_cuboid(0,0,0), 0)

    def test_volume_cuboid_non_numeric(self):
        with self.assertRaises(TypeError):
            volume_cuboid('a','b','c')

    def test_volume_cuboid_non_numeric2(self):
        with self.assertRaises(TypeError):
            volume_cuboid(1,'b',3)

    def test_volume_cuboid_non_numeric3(self):
        with self.assertRaises(TypeError):
            volume_cuboid(1,2,'c')
