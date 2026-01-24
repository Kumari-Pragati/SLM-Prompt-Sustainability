import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(lateralsurface_cube(1), 4)
        self.assertEqual(lateralsurface_cube(2), 16)
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_edge_cases(self):
        self.assertEqual(lateralsurface_cube(0), 0)
        self.assertEqual(lateralsurface_cube(1e-5), 4 * (1e-5 * 1e-5))
        self.assertEqual(lateralsurface_cube(1e6), 4 * (1e6 * 1e6))
