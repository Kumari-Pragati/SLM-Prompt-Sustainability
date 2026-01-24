import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_zero_dimensions(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)

    def test_one_dimension(self):
        self.assertEqual(surfacearea_cuboid(1, 0, 0), 0)
        self.assertEqual(surfacearea_cuboid(0, 1, 0), 0)
        self.assertEqual(surfacearea_cuboid(0, 0, 1), 0)

    def test_simple_cuboid(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 144)

    def test_negative_dimensions(self):
        self.assertEqual(surfacearea_cuboid(-1, 2, 3), 30)
        self.assertEqual(surfacearea_cuboid(2, -3, 4), 30)
        self.assertEqual(surfacearea_cuboid(2, 3, -4), 30)

    def test_float_dimensions(self):
        self.assertAlmostEqual(surfacearea_cuboid(2.5, 3.2, 4.1), 146.6)
