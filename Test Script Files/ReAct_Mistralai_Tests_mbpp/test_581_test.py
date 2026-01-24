import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_positive_base_and_side(self):
        self.assertEqual(surface_Area(3, 4), 38)

    def test_zero_base(self):
        self.assertEqual(surface_Area(0, 4), 0)

    def test_zero_side(self):
        self.assertEqual(surface_Area(3, 0), 9)

    def test_negative_base(self):
        self.assertEqual(surface_Area(-3, 4), -18)

    def test_negative_side(self):
        self.assertEqual(surface_Area(3, -4), 25)

    def test_floating_point_base(self):
        self.assertAlmostEqual(surface_Area(3.5, 4), 32.25)

    def test_floating_point_side(self):
        self.assertAlmostEqual(surface_Area(3, 4.5), 32.25)
