import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(surfacearea_cuboid(2,3,4), 52)
        self.assertEqual(surfacearea_cuboid(5,5,5), 150)
        self.assertEqual(surfacearea_cuboid(10,10,10), 600)

    def test_negative_numbers(self):
        self.assertEqual(surfacearea_cuboid(-2,-3,-4), 52)
        self.assertEqual(surfacearea_cuboid(-5,-5,-5), 150)
        self.assertEqual(surfacearea_cuboid(-10,-10,-10), 600)

    def test_zero(self):
        self.assertEqual(surfacearea_cuboid(0,0,0), 0)
        self.assertEqual(surfacearea_cuboid(0,5,10), 100)
        self.assertEqual(surfacearea_cuboid(5,0,10), 100)
        self.assertEqual(surfacearea_cuboid(5,10,0), 100)

    def test_decimal_numbers(self):
        self.assertEqual(surfacearea_cuboid(2.5,3.5,4.5), 61)
        self.assertEqual(surfacearea_cuboid(5.5,5.5,5.5), 175)
        self.assertEqual(surfacearea_cuboid(10.5,10.5,10.5), 635)
