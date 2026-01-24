import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(surfacearea_cuboid(1, 2, 3), 2*(1*2 + 1 * 3 + 2 * 3))
        self.assertEqual(surfacearea_cuboid(4, 5, 6), 2*(4*5 + 4 * 6 + 5 * 6))
        self.assertEqual(surfacearea_cuboid(7, 8, 9), 2*(7*8 + 7 * 9 + 8 * 9))

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 2*(1*1 + 1 * 1 + 1 * 1))
        self.assertEqual(surfacearea_cuboid(10, 10, 10), 2*(10*10 + 10 * 10 + 10 * 10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid('a', 2, 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, 'b', 3)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(1, 2, 'c')
