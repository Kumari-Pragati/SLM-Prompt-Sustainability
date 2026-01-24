import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(surfacearea_cuboid(3, 4, 5), 94.0)

    def test_zero_dimensions(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            surfacearea_cuboid(-1, 2, 3)

    def test_large_numbers(self):
        self.assertAlmostEqual(surfacearea_cuboid(1000, 1000, 1000), 6000000.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid("a", 2, 3)
