import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsurface_cuboid(3, 4, 5), 56.0)

    def test_zero_dimensions(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(Exception):
            lateralsurface_cuboid(-1, 2, 3)

    def test_large_dimensions(self):
        self.assertAlmostEqual(lateralsurface_cuboid(10000, 10000, 10000), 60000000.0)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception):
            lateralsurface_cuboid('a', 2, 3)
