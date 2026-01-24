import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_surfacearea_cube(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(3), 54)
        self.assertEqual(surfacearea_cube(4), 80)
        self.assertEqual(surfacearea_cube(5), 110)

    def test_surfacearea_cube_negative(self):
        self.assertRaises(TypeError, surfacearea_cube, -1)

    def test_surfacearea_cube_non_integer(self):
        self.assertRaises(TypeError, surfacearea_cube, 3.5)
