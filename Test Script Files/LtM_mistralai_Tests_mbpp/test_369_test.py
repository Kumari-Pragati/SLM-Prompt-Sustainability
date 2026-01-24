import unittest
from mbpp_369_code import lateralsurface_cuboid

class TestLateralSurfaceCuboid(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(lateralsurface_cuboid(1, 2, 3), 12)
        self.assertEqual(lateralsurface_cuboid(2, 3, 4), 28)
        self.assertEqual(lateralsurface_cuboid(3, 4, 5), 42)

    def test_edge_input(self):
        self.assertEqual(lateralsurface_cuboid(0, 1, 2), 6)
        self.assertEqual(lateralsurface_cuboid(1, 0, 2), 6)
        self.assertEqual(lateralsurface_cuboid(1, 1, 0), 0)
        self.assertEqual(lateralsurface_cuboid(1, 2, 0), 12)
        self.assertEqual(lateralsurface_cuboid(2, 1, 0), 12)
        self.assertEqual(lateralsurface_cuboid(0, 0, 1), 0)

    def test_boundary_input(self):
        self.assertEqual(lateralsurface_cuboid(float('inf'), 1, 2), 10 * float('inf'))
        self.assertEqual(lateralsurface_cuboid(1, float('inf'), 2), 10 * float('inf'))
        self.assertEqual(lateralsurface_cuboid(1, 1, float('inf')), 2 * float('inf'))
        self.assertEqual(lateralsurface_cuboid(float('-inf'), 1, 2), -10 * float('inf'))
        self.assertEqual(lateralsurface_cuboid(1, float('-inf'), 2), -10 * float('inf'))
        self.assertEqual(lateralsurface_cuboid(1, 1, float('-inf')), -2 * float('inf'))
