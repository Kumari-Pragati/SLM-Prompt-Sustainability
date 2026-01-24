import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(surfacearea_cube(1), 6)
        self.assertEqual(surfacearea_cube(2), 24)
        self.assertEqual(surfacearea_cube(3), 54)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(surfacearea_cube(0), 0)
        self.assertEqual(surfacearea_cube(1e-5), 6*1e-5)
        self.assertEqual(surfacearea_cube(1e6), 6*1e6)

    def test_negative_input(self):
        self.assertEqual(surfacearea_cube(-1), None)
