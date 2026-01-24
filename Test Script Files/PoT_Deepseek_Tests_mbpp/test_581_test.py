import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(surface_Area(2, 3), 20)

    def test_edge_case_zero_base(self):
        self.assertEqual(surface_Area(0, 5), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(surface_Area(4, 0), 16)

    def test_boundary_case_negative_base(self):
        with self.assertRaises(Exception):
            surface_Area(-2, 3)

    def test_boundary_case_negative_height(self):
        with self.assertRaises(Exception):
            surface_Area(2, -3)

    def test_corner_case_large_numbers(self):
        self.assertEqual(surface_Area(1000, 1000), 2000000)
