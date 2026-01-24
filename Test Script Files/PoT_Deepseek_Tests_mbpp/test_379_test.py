import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(surfacearea_cuboid(1, 2, 3), 22)

    def test_edge_case(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)

    def test_corner_case(self):
        self.assertEqual(surfacearea_cuboid(100, 100, 100), 6000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid("1", 2, 3)
