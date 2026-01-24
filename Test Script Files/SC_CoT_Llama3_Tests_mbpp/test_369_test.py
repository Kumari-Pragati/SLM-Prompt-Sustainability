import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(4, 5, 6), 24)

    def test_edge_cases(self):
        self.assertEqual(lateralsurface_cuboid(0, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(1, 0, 3), 6)
        self.assertEqual(lateralsurface_cuboid(1, 2, 0), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid('a', 2, 3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1, 'b', 3)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(1, 2, 'c')

    def test_corner_cases(self):
        self.assertEqual(lateralsurface_cuboid(1, 1, 1), 8)
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)
