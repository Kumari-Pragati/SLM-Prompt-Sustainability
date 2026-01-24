import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_lateralsurface_cube_positive_number(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_lateralsurface_cube_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_lateralsurface_cube_negative_number(self):
        self.assertEqual(lateralsurface_cube(-3), 36)

    def test_lateralsurface_cube_non_integer(self):
        self.assertEqual(lateralsurface_cube(2.5), 20)

    def test_lateralsurface_cube_large_number(self):
        self.assertEqual(lateralsurface_cube(1000), 4000000)
