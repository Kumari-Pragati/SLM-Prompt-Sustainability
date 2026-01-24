import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(volume_cuboid(3, 4, 5), 60)

    def test_zero_length(self):
        self.assertEqual(volume_cuboid(0, 4, 5), 0)

    def test_zero_width(self):
        self.assertEqual(volume_cuboid(3, 0, 5), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cuboid(3, 4, 0), 0)

    def test_negative_length(self):
        with self.assertRaises(TypeError):
            volume_cuboid(-3, 4, 5)

    def test_negative_width(self):
        with self.assertRaises(TypeError):
            volume_cuboid(3, -4, 5)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            volume_cuboid(3, 4, -5)
