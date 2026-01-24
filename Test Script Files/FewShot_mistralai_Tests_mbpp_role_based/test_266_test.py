import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralSurfaceCube(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_number(self):
        self.assertEqual(lateralsurface_cube(-1), 1)

    def test_large_number(self):
        self.assertEqual(lateralsurface_cube(1000), 1000000000)
