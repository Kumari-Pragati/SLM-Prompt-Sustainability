import unittest
from mbpp_373_code import volume_cuboid

class TestVolumeCuboid(unittest.TestCase):

    def test_positive_typical_case(self):
        self.assertEqual(volume_cuboid(2, 3, 4), 24)

    def test_zero_length(self):
        self.assertEqual(volume_cuboid(0, 3, 4), 0)

    def test_zero_width(self):
        self.assertEqual(volume_cuboid(2, 0, 4), 0)

    def test_zero_height(self):
        self.assertEqual(volume_cuboid(2, 3, 0), 0)

    def test_negative_length(self):
        self.assertEqual(volume_cuboid(-2, 3, 4), -24)

    def test_negative_width(self):
        self.assertEqual(volume_cuboid(2, -3, 4), -24)

    def test_negative_height(self):
        self.assertEqual(volume_cuboid(2, 3, -4), -24)

    def test_float_length(self):
        self.assertAlmostEqual(volume_cuboid(2.5, 3, 4), 72)

    def test_float_width(self):
        self.assertAlmostEqual(volume_cuboid(2, 3.5, 4), 72)

    def test_float_height(self):
        self.assertAlmostEqual(volume_cuboid(2, 3, 4.5), 72)

    def test_mixed_floats_and_ints(self):
        self.assertAlmostEqual(volume_cuboid(2, 3.5, 4), 72)
