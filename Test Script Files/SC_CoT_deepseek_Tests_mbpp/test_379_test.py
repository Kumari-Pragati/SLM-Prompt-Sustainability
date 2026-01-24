import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cuboid(3, 4, 5), 94.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertAlmostEqual(surfacearea_cuboid(1, 1, 1), 6.0)

    def test_edge_case(self):
        self.assertAlmostEqual(surfacearea_cuboid(1, 2, 3), 22.0)
        self.assertAlmostEqual(surfacearea_cuboid(10, 10, 10), 600.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, 4, "5")
        with self.assertRaises(TypeError):
            surfacearea_cuboid("3", "4", "5")
        with self.assertRaises(ValueError):
            surfacearea_cuboid(-1, 4, 5)
        with self.assertRaises(ValueError):
            surfacearea_cuboid(3, -4, 5)
        with self.assertRaises(ValueError):
            surfacearea_cuboid(3, 4, -5)
