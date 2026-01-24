import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_cube(5), 150)

    def test_edge_case_zero(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            surfacearea_cube(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            surfacearea_cube('five')

    def test_edge_case_large(self):
        self.assertEqual(surfacearea_cube(100), 360000)
