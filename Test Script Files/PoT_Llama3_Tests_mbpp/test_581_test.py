import unittest
from mbpp_581_code import surface_Area

class TestSurfaceArea(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(surface_Area(5, 3), 62)

    def test_edge_case_zero_side(self):
        self.assertEqual(surface_Area(5, 0), 25)

    def test_edge_case_zero_base(self):
        self.assertEqual(surface_Area(0, 3), 0)

    def test_edge_case_zero_base_and_side(self):
        self.assertEqual(surface_Area(0, 0), 0)

    def test_edge_case_negative_base(self):
        self.assertEqual(surface_Area(-5, 3), 62)

    def test_edge_case_negative_side(self):
        self.assertEqual(surface_Area(5, -3), 62)

    def test_edge_case_negative_base_and_side(self):
        self.assertEqual(surface_Area(-5, -3), 62)

    def test_edge_case_zero_base_and_negative_side(self):
        self.assertEqual(surface_Area(0, -3), 0)

    def test_edge_case_negative_base_and_zero_side(self):
        self.assertEqual(surface_Area(-5, 0), 25)

    def test_edge_case_negative_base_and_negative_side(self):
        self.assertEqual(surface_Area(-5, -3), 62)
