import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_lateralsurface_cube_positive(self):
        self.assertEqual(lateralsurface_cube(2), 16)

    def test_lateralsurface_cube_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(-2)

    def test_lateralsurface_cube_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_lateralsurface_cube_non_numeric(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube('a')
