import unittest
from mbpp_266_code import lateralsurface_cube

class TestLateralsurfaceCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lateralsurface_cube(5), 100)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(0), 0)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(-5), 0)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(10), 400)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(20), 800)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(-20), 800)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(100), 40000)

    def test_edge_case(self):
        self.assertEqual(lateralsurface_cube(-100), 40000)
