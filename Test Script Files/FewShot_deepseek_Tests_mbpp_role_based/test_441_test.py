import unittest
from mbpp_441_code import surfacearea_cube

class TestSurfaceAreaCube(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(surfacearea_cube(5), 150)

    def test_edge_condition(self):
        self.assertEqual(surfacearea_cube(0), 0)

    def test_boundary_condition(self):
        self.assertEqual(surfacearea_cube(1), 6)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            surfacearea_cube(-1)
