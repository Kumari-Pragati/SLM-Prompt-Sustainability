import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_surface_area_cube_positive(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(3), 54)
        self.assertEqual(surfacearea_cube(4), 96)
        self.assertEqual(surfacearea_cube(5), 150)

    def test_surface_area_cube_zero(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_surface_area_cube_negative(self):
        self.assertEqual(surfacearea_cube(-1), 6)
        self.assertEqual(surfacearea_cube(-2), 24)
        self.assertEqual(surfacearea_cube(-3), 54)
        self.assertEqual(surfacearea_cube(-4), 96)
        self.assertEqual(surfacearea_cube(-5), 150)
