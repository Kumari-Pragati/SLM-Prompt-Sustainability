import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_cuboid(5, 3, 2), 62)

    def test_edge_case(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)

    def test_edge_case2(self):
        self.assertEqual(surfacearea_cuboid(10, 10, 10), 800)

    def test_edge_case3(self):
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 12)

    def test_edge_case4(self):
        self.assertEqual(surfacearea_cuboid(-1, -1, -1), 12)

    def test_edge_case5(self):
        self.assertEqual(surfacearea_cuboid(1, 0, 0), 4)

    def test_edge_case6(self):
        self.assertEqual(surfacearea_cuboid(0, 1, 0), 4)

    def test_edge_case7(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 1), 4)
