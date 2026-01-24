import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 56)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid('a', 3, 4)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(2, 'b', 4)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(2, 3, 'c')

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(-1, 3, 4), 56)
        self.assertEqual(surfacearea_cuboid(2, -1, 4), 56)
        self.assertEqual(surfacearea_cuboid(2, 3, -1), 56)
