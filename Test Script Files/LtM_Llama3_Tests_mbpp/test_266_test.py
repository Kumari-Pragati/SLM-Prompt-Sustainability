import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(lateralsurface_cube(2), 16)

    def test_zero_input(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_negative_input(self):
        self.assertEqual(lateralsurface_cube(-2), 16)

    def test_non_integer_input(self):
        self.assertEqual(lateralsurface_cube(2.5), 16)

    def test_edge_case_input(self):
        self.assertEqual(lateralsurface_cube(10), 400)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lateralsurface_cube("a")
