import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 52)
        self.assertEqual(surfacearea_cuboid(5, 6, 7), 224)
        self.assertEqual(surfacearea_cuboid(10, 10, 10), 600)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 3, 4), 24)
        self.assertEqual(surfacearea_cuboid(3, 0, 4), 24)
        self.assertEqual(surfacearea_cuboid(3, 3, 0), 24)
        self.assertEqual(surfacearea_cuboid(3, 3, 3), 54)

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 6)
        self.assertEqual(surfacearea_cuboid(1, 1, 2), 12)
        self.assertEqual(surfacearea_cuboid(1, 2, 1), 12)
        self.assertEqual(surfacearea_cuboid(2, 1, 1), 12)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, surfacearea_cuboid, 'a', 3, 4)
        self.assertRaises(TypeError, surfacearea_cuboid, 3, 'b', 4)
        self.assertRaises(TypeError, surfacearea_cuboid, 3, 4, 'c')
