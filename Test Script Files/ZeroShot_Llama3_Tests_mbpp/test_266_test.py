import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_lateralsurface_cube_positive(self):
        self.assertEqual(lateralsurface_cube(1), 16)
        self.assertEqual(lateralsurface_cube(2), 32)
        self.assertEqual(lateralsurface_cube(3), 48)
        self.assertEqual(lateralsurface_cube(4), 64)
        self.assertEqual(lateralsurface_cube(5), 80)

    def test_lateralsurface_cube_negative(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(-1)
        with self.assertRaises(TypeError):
            lateralsurface_cube(-2)
        with self.assertRaises(TypeError):
            lateralsurface_cube(-3)

    def test_lateralsurface_cube_non_integer(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(1.5)
        with self.assertRaises(TypeError):
            lateralsurface_cube(2.5)
