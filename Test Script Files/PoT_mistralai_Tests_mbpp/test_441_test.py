import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surfacearea_cube(3), 54)

    def test_edge_case_zero(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(surfacearea_cube(1), 6)

    def test_edge_case_negative(self):
        self.assertEqual(surfacearea_cube(-1), None)

    def test_boundary_case_half(self):
        self.assertEqual(surfacearea_cube(0.5), 3)
