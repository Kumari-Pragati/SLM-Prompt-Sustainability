import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_zero(self):
        self.assertEqual(volume_cuboid(0, 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(volume_cuboid(-1, -2, -3), 12)

    def test_mixed_numbers(self):
        self.assertEqual(volume_cuboid(2, -3, 4), -24)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(volume_cuboid(0, -1, -2), 0)
