import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_zero(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            lateralsurface_cube(-3)

    def test_large_number(self):
        self.assertEqual(lateralsurface_cube(1000), 4000000)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(3.5)
