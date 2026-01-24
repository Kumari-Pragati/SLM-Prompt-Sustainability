import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surface_Area(2, 3), 20)

    def test_edge_case_zero(self):
        self.assertEqual(surface_Area(0, 3), 0)
        self.assertEqual(surface_Area(2, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(surface_Area(1, 1), 6)

    def test_edge_case_negative(self):
        self.assertEqual(surface_Area(-1, 2), 0)
        self.assertEqual(surface_Area(2, -1), 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, surface_Area, -2, 3)
        self.assertRaises(ValueError, surface_Area, 2, -3)
        self.assertRaises(ValueError, surface_Area, 0, 0)
