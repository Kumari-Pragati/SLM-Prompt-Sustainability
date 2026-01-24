import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_positive_base_and_side(self):
        self.assertEqual(surface_Area(3, 4), 30)

    def test_zero_base(self):
        self.assertEqual(surface_Area(0, 4), 0)

    def test_zero_side(self):
        self.assertEqual(surface_Area(3, 0), 0)

    def test_negative_base(self):
        self.assertEqual(surface_Area(-3, 4), 36)

    def test_negative_side(self):
        self.assertEqual(surface_Area(3, -4), 36)
