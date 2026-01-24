import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cube(1), 6)
        self.assertEqual(lateralsurface_cube(2), 16)
        self.assertEqual(lateralsurface_cube(3), 28)

    def test_edge_case_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(lateralsurface_cube(-1), 1)
