import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(lateralsurface_cuboid(2, 3, 4), 32)

    def test_zero_length(self):
        self.assertEqual(lateralsurface_cuboid(0, 3, 4), 0)

    def test_zero_width(self):
        self.assertEqual(lateralsurface_cuboid(2, 0, 4), 0)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cuboid(2, 3, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(lateralsurface_cuboid(-2, 3, 4), -24)
