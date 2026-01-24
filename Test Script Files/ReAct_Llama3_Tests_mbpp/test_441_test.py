import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(surfacearea_cube(5), 150)

    def test_edge_case(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_negative_case(self):
        with self.assertRaises(TypeError):
            surfacearea_cube(-5)

    def test_non_numeric_case(self):
        with self.assertRaises(TypeError):
            surfacearea_cube('five')
