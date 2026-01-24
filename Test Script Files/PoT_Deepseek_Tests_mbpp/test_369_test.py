import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralsurfaceCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 56)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cuboid(0, 0, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(lateralsurface_cuboid(1, 1, 1), 8)

    def test_corner_case(self):
        self.assertEqual(lateralsurface_cuboid(100, 100, 100), 6000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lateralsurface_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            lateralsurface_cuboid(3, 4, "5")
