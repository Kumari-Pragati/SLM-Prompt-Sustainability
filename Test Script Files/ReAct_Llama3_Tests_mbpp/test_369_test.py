import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(5, 3, 2), 20)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cuboid(0, 3, 2), 12)
        self.assertEqual(lateralsurface_cuboid(5, 0, 2), 12)
        self.assertEqual(lateralsurface_cuboid(5, 3, 0), 12)

    def test_negative_values(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(-5, 3, 2)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(5, -3, 2)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(5, 3, -2)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid('a', 3, 2)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(5, 'b', 2)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(5, 3, 'c')
