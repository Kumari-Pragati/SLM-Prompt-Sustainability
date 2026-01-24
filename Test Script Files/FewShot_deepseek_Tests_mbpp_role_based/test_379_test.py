import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(surfacearea_cuboid(3, 4, 5), 94)

    def test_edge_conditions(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(1, 1, 1), 6)

    def test_boundary_conditions(self):
        self.assertEqual(surfacearea_cuboid(0, 10, 20), 0)
        self.assertEqual(surfacearea_cuboid(10, 0, 20), 0)
        self.assertEqual(surfacearea_cuboid(10, 20, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid("3", 4, 5)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, "4", 5)
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, 4, "5")
        with self.assertRaises(ValueError):
            surfacearea_cuboid(-1, 4, 5)
        with self.assertRaises(ValueError):
            surfacearea_cuboid(3, -4, 5)
        with self.assertRaises(ValueError):
            surfacearea_cuboid(3, 4, -5)
