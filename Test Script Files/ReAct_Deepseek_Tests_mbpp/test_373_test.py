import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(volume_cuboid(3, 4, 5), 60)

    def test_zero_dimensions(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(Exception):
            volume_cuboid(-1, 2, 3)

    def test_large_numbers(self):
        self.assertEqual(volume_cuboid(1000, 1000, 1000), 1000000000)

    def test_non_integer_dimensions(self):
        self.assertAlmostEqual(volume_cuboid(2.5, 3.5, 4.5), 41.25)
