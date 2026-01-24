import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_surfacearea_cube_typical(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(3), 54)

    def test_surfacearea_cube_edge(self):
        self.assertEqual(surfacearea_cube(0), 0)
        self.assertEqual(surfacearea_cube(1), 6)

    def test_surfacearea_cube_boundary(self):
        self.assertEqual(surfacearea_cube(100), 6000)
        self.assertEqual(surfacearea_cube(1000), 6000000)

    def test_surfacearea_cube_invalid(self):
        with self.assertRaises(TypeError):
            surfacearea_cube("1")
        with self.assertRaises(ValueError):
            surfacearea_cube(-1)
