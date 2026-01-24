import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 56)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)
        self.assertEqual(surfacearea_cuboid(10, 10, 10), 240)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid(-1, 2, 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, -2, 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, 2, -3)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid('a', 2, 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, 'b', 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, 2, 'c')
