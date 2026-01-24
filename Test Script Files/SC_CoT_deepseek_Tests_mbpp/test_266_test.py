import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lateralsurface_cube(3), 36)

    def test_boundary_case(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(1), 4)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            lateralsurface_cube(-1)

    def test_non_numeric_input(self):
        with self.assertRaises(Exception):
            lateralsurface_cube("abc")
