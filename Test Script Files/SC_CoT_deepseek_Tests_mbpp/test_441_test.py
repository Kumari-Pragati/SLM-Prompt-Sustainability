import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(surfacearea_cube(5), 150)

    def test_edge_case(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_boundary_case(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(100), 60000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            surfacearea_cube("5")
        with self.assertRaises(ValueError):
            surfacearea_cube(-5)
