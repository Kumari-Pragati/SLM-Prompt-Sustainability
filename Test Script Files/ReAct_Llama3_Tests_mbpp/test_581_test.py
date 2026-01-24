import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surface_Area(2, 3), 18)

    def test_zero_base(self):
        self.assertEqual(surface_Area(0, 3), 0)

    def test_zero_side(self):
        self.assertEqual(surface_Area(2, 0), 0)

    def test_zero_base_and_side(self):
        self.assertEqual(surface_Area(0, 0), 0)

    def test_negative_base(self):
        self.assertEqual(surface_Area(-2, 3), 12)

    def test_negative_side(self):
        self.assertEqual(surface_Area(2, -3), 12)

    def test_negative_base_and_side(self):
        self.assertEqual(surface_Area(-2, -3), 12)

    def test_non_integer_base(self):
        self.assertAlmostEqual(surface_Area(2.5, 3), 17.5)

    def test_non_integer_side(self):
        self.assertAlmostEqual(surface_Area(2, 3.5), 17.5)

    def test_non_integer_base_and_side(self):
        self.assertAlmostEqual(surface_Area(2.5, 3.5), 17.5)
