import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lateralsurface_cube(1), 4)
        self.assertEqual(lateralsurface_cube(2), 16)
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lateralsurface_cube(0), 0)
        self.assertEqual(lateralsurface_cube(100), 40000)

    def test_corner_cases(self):
        self.assertEqual(lateralsurface_cube(0.5), 2)
        self.assertEqual(lateralsurface_cube(0.1), 0.4)
