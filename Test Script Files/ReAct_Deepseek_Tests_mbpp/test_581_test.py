import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(surface_Area(5, 10), 150)

    def test_zero_base(self):
        self.assertEqual(surface_Area(0, 10), 0)

    def test_zero_height(self):
        self.assertEqual(surface_Area(5, 0), 25)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            surface_Area(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            surface_Area(5, -10)

    def test_zero_dimensions(self):
        self.assertEqual(surface_Area(0, 0), 0)
