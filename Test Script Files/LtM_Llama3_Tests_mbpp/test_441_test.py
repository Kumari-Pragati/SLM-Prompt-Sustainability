import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(3), 54)

    def test_edge_cases(self):
        self.assertEqual(surfacearea_cube(0), 0)
        self.assertEqual(surfacearea_cube(-1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            surfacearea_cube('a')
