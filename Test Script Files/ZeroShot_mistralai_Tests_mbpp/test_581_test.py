import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_surface_area_simple(self):
        self.assertEqual(surface_Area(2, 3), 20)

    def test_surface_area_zero(self):
        self.assertEqual(surface_Area(0, 3), 0)

    def test_surface_area_negative(self):
        self.assertEqual(surface_Area(-2, 3), 12)

    def test_surface_area_one(self):
        self.assertEqual(surface_Area(1, 1), 4)
