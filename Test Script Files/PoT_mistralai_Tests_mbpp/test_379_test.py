import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(surfacearea_cuboid(1, 2, 3), 38)
        self.assertEqual(surfacearea_cuboid(4, 5, 6), 168)
        self.assertEqual(surfacearea_cuboid(7, 8, 9), 274)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 2, 3), 12)
        self.assertEqual(surfacearea_cuboid(1, 0, 3), 12)
        self.assertEqual(surfacearea_cuboid(1, 2, 0), 12)
        self.assertEqual(surfacearea_cuboid(1, 2, 1), 12)

    def test_boundary_cases(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)
        self.assertEqual(surfacearea_cuboid(1, 2, 1), 12)
        self.assertEqual(surfacearea_cuboid(2, 1, 1), 12)
