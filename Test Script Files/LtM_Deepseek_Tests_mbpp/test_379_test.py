import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 6)
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 52)
        self.assertEqual(surfacearea_cuboid(5, 5, 5), 150)

    def test_edge_conditions(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(0, 1, 1), 4)
        self.assertEqual(surfacearea_cuboid(1, 0, 1), 4)
        self.assertEqual(surfacearea_cuboid(1, 1, 0), 4)

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 10000), 20004)
        self.assertEqual(surfacearea_cuboid(10000, 1, 1), 20004)
        self.assertEqual(surfacearea_cuboid(10000, 10000, 1), 20004)
        self.assertEqual(surfacearea_cuboid(10000, 1, 10000), 20004)

    def test_complex_cases(self):
        self.assertEqual(surfacearea_cuboid(3, 2, 5), 52)
        self.assertEqual(surfacearea_cuboid(10, 10, 10), 600)
