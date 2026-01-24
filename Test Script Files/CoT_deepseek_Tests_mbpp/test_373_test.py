import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(volume_cuboid(3, 4, 5), 60)

    def test_zero_dimensions(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)
        self.assertEqual(volume_cuboid(0, 5, 10), 0)
        self.assertEqual(volume_cuboid(3, 0, 7), 0)
        self.assertEqual(volume_cuboid(0, 4, 8), 0)

    def test_negative_dimensions(self):
        self.assertEqual(volume_cuboid(-3, 4, 5), -60)
        self.assertEqual(volume_cuboid(3, -4, 5), -60)
        self.assertEqual(volume_cuboid(3, 4, -5), -60)

    def test_large_numbers(self):
        self.assertEqual(volume_cuboid(1000000000, 1000000000, 1000000000), 1000000000000000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            volume_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            volume_cuboid(3, 4, "5")
        with self.assertRaises(TypeError):
            volume_cuboid("3", "4", "5")
