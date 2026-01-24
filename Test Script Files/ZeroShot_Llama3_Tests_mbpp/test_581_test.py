import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_surface_area_positive(self):
        self.assertEqual(surface_Area(5, 3), 64)

    def test_surface_area_negative(self):
        with self.assertRaises(TypeError):
            surface_Area(-5, 3)

    def test_surface_area_zero(self):
        self.assertEqual(surface_Area(0, 0), 0)

    def test_surface_area_non_numeric(self):
        with self.assertRaises(TypeError):
            surface_Area('five', 3)

    def test_surface_area_non_numeric2(self):
        with self.assertRaises(TypeError):
            surface_Area(5, 'three')
