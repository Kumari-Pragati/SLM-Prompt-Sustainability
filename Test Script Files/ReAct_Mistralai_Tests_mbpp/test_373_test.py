import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_positive_typical_case(self):
        "Test volume calculation with positive typical values"
        length = 5
        width = 3
        height = 7
        expected_volume = 105
        self.assertEqual(volume_cuboid(length, width, height), expected_volume)

    def test_zero_length(self):
        "Test volume calculation with zero length"
        length = 0
        width = 3
        height = 7
        expected_volume = 0
        self.assertEqual(volume_cuboid(length, width, height), expected_volume)

    def test_negative_length(self):
        "Test volume calculation with negative length"
        length = -3
        width = 3
        height = 7
        with self.assertRaises(ValueError):
            volume_cuboid(length, width, height)

    def test_zero_width(self):
        "Test volume calculation with zero width"
        length = 3
        width = 0
        height = 7
        expected_volume = 0
        self.assertEqual(volume_cuboid(length, width, height), expected_volume)

    def test_negative_width(self):
        "Test volume calculation with negative width"
        length = 3
        width = -3
        height = 7
        with self.assertRaises(ValueError):
            volume_cuboid(length, width, height)

    def test_zero_height(self):
        "Test volume calculation with zero height"
        length = 3
        width = 3
        height = 0
        expected_volume = 0
        self.assertEqual(volume_cuboid(length, width, height), expected_volume)

    def test_negative_height(self):
        "Test volume calculation with negative height"
        length = 3
        width = 3
        height = -3
        with self.assertRaises(ValueError):
            volume_cuboid(length, width, height)
