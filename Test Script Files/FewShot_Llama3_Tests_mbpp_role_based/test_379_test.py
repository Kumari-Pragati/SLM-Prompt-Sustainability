import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(surfacearea_cuboid(3, 4, 5), 92)

    def test_zero_length(self):
        self.assertEqual(surfacearea_cuboid(0, 4, 5), 40)

    def test_zero_width(self):
        self.assertEqual(surfacearea_cuboid(3, 0, 5), 30)

    def test_zero_height(self):
        self.assertEqual(surfacearea_cuboid(3, 4, 0), 24)

    def test_negative_length(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid(-3, 4, 5)

    def test_negative_width(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, -4, 5)

    def test_negative_height(self):
        with self.assertRaises(TypeError):
            surfacearea_cuboid(3, 4, -5)
