import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):

    def test_lateral_surface_cube_positive(self):
        self.assertEqual(lateralsurface_cube(1), 6.0)
        self.assertEqual(lateralsurface_cube(2), 24.0)
        self.assertEqual(lateralsurface_cube(3), 54.0)
        self.assertEqual(lateralsurface_cube(4), 80.0)
        self.assertEqual(lateralsurface_cube(5), 100.0)

    def test_lateral_surface_cube_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0.0)

    def test_lateral_surface_cube_negative(self):
        self.assertEqual(lateralsurface_cube(-1), -6.0)
        self.assertEqual(lateralsurface_cube(-2), -24.0)
        self.assertEqual(lateralsurface_cube(-3), -54.0)
        self.assertEqual(lateralsurface_cube(-4), -80.0)
        self.assertEqual(lateralsurface_cube(-5), -100.0)
