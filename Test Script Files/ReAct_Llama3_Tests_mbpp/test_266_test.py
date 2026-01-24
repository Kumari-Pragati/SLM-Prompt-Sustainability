import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):
    def test_positive_lateral(self):
        self.assertEqual(lateralsurface_cube(5), 100)

    def test_zero_lateral(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_lateral(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(-5)

    def test_non_numeric_lateral(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube('five')
