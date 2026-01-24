import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(surfacearea_cuboid(2, 3, 4), 52)

    def test_zero(self):
        self.assertEqual(surfacearea_cuboid(0, 0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(surfacearea_cuboid(-1, -2, -3), 30)

    def test_one_zero_and_negative(self):
        self.assertEqual(surfacearea_cuboid(1, 0, -3), 12)

    def test_one_negative_and_zero(self):
        self.assertEqual(surfacearea_cuboid(-1, 0, -3), 12)

    def test_one_and_zero(self):
        self.assertEqual(surfacearea_cuboid(1, 0, 3), 12)

    def test_zero_and_one(self):
        self.assertEqual(surfacearea_cuboid(0, 1, 3), 12)
