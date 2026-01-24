import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 52)
        self.assertEqual(surfacearea_cuboid(5, 6, 7), 224)
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(0, 3, 4), 24)
        self.assertEqual(surfacearea_cuboid(3, 0, 4), 24)
        self.assertEqual(surfacearea_cuboid(3, 3, 0), 24)
        self.assertEqual(surfacearea_cuboid(3, 3, 3), 54)

    def test_negative_inputs(self):
        self.assertEqual(surfacearea_cuboid(-1, 3, 4), None)
        self.assertEqual(surfacearea_cuboid(3, -1, 4), None)
        self.assertEqual(surfacearea_cuboid(3, 3, -1), None)
