import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 60)

    def test_zero_length(self):
        self.assertEqual(lateralsurface_cuboid(0, 4, 5), 40)

    def test_zero_width(self):
        self.assertEqual(lateralsurface_cuboid(3, 0, 5), 40)

    def test_zero_height(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 0), 8)

    def test_negative_length(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(-3, 4, 5)

    def test_negative_width(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, -4, 5)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, 4, -5)
