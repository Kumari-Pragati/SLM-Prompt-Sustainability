import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(lateralsurface_cube(2), 16)
        self.assertEqual(lateralsurface_cube(3), 36)
        self.assertEqual(lateralsurface_cube(4), 64)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lateralsurface_cube(0), 0)
        self.assertEqual(lateralsurface_cube(1), 4)
        self.assertEqual(lateralsurface_cube(5), 100)
        self.assertEqual(lateralsurface_cube(-1), 1)
        self.assertEqual(lateralsurface_cube(-2), 8)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube('str')
        with self.assertRaises(TypeError):
            lateralsurface_cube([1, 2, 3])
