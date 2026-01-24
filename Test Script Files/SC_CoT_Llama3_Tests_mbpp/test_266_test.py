import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(lateralsurface_cube(5), 100)

    def test_zero_input(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube(-5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube('five')

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(1), 4)

    def test_large_input(self):
        self.assertEqual(lateralsurface_cube(10), 400)
