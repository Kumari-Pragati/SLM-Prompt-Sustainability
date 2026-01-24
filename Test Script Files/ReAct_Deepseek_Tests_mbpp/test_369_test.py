import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 44)

    def test_zero_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(Exception):
            lateralsurface_cuboid(-1, 2, 3)

    def test_large_numbers(self):
        self.assertEqual(lateralsurface_cuboid(1000, 1000, 1000), 6000000)

    def test_non_integer_dimensions(self):
        self.assertAlmostEqual(lateralsurface_cuboid(3.5, 4.5, 5.5), 44.0)
