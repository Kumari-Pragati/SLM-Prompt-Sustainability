import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(surfacearea_cube(3), 54)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(surfacearea_cube(0), 0)
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2**32), 248832048)

    def test_negative_input(self):
        self.assertRaises(ValueError, surfacearea_cube, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, surfacearea_cube, 2.5)
