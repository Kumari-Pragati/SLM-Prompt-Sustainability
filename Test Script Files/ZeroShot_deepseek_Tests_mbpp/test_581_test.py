import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(surface_Area(2,3), 20)
        self.assertEqual(surface_Area(5,7), 70)
        self.assertEqual(surface_Area(10,15), 250)

    def test_negative_numbers(self):
        self.assertEqual(surface_Area(-2,-3), 20)
        self.assertEqual(surface_Area(-5,-7), 70)
        self.assertEqual(surface_Area(-10,-15), 250)

    def test_zero(self):
        self.assertEqual(surface_Area(0,0), 0)
        self.assertEqual(surface_Area(0,5), 0)
        self.assertEqual(surface_Area(7,0), 49)

    def test_decimal_numbers(self):
        self.assertEqual(surface_Area(2.5,3.5), 24.5)
        self.assertEqual(surface_Area(5.2,7.3), 59.6)
        self.assertEqual(surface_Area(10.1,15.2), 255.2)
