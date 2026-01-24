import unittest
from mbpp_379_code import surfacearea_cuboid

class TestSurfaceAreaCuboid(unittest.TestCase):

    def test_surface_area_cuboid(self):
        self.assertEqual(surfacearea_cuboid(1,1,1), 6)
        self.assertEqual(surfacearea_cuboid(2,3,4), 24)
        self.assertEqual(surfacearea_cuboid(5,5,5), 50)
        self.assertEqual(surfacearea_cuboid(10,10,10), 80)
        self.assertEqual(surfacearea_cuboid(1,2,3), 16)
        self.assertEqual(surfacearea_cuboid(4,5,6), 36)
        self.assertEqual(surfacearea_cuboid(7,8,9), 72)
