import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_simple_cuboid(self):
        self.assertEqual(surfacearea_cuboid(1, 2, 3), 36)
        self.assertEqual(surfacearea_cuboid(2, 2, 2), 24)
        self.assertEqual(surfacearea_cuboid(3, 3, 3), 54)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 2, 3), 18)
        self.assertEqual(surfacearea_cuboid(1, 0, 3), 18)
        self.assertEqual(surfacearea_cuboid(1, 2, 0), 18)
        self.assertEqual(surfacearea_cuboid(0, 0, 3), 0)
        self.assertEqual(surfacearea_cuboid(1, 2, 0), 18)
        self.assertEqual(surfacearea_cuboid(0, 2, 1), 10)
        self.assertEqual(surfacearea_cuboid(1, 0, 1), 10)
        self.assertEqual(surfacearea_cuboid(0, 1, 1), 10)

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)
        self.assertEqual(surfacearea_cuboid(-1, 2, 3), 36)
        self.assertEqual(surfacearea_cuboid(1, -2, 3), 36)
        self.assertEqual(surfacearea_cuboid(1, 2, -3), 36)
