import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_case(self):
        polygons = calculate_polygons(0, 0, 10, 10, 2)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_startx_zero(self):
        polygons = calculate_polygons(0, 0, 5, 10, 2)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_starty_zero(self):
        polygons = calculate_polygons(0, 0, 10, 5, 2)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_endx_zero(self):
        polygons = calculate_polygons(5, 5, 0, 10, 2)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_endy_zero(self):
        polygons = calculate_polygons(0, 5, 10, 0, 2)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_radius_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_polygons(0, 0, 10, 10, 0)

    def test_edge_case_startx_endx_equal(self):
        polygons = calculate_polygons(5, 5, 5, 10, 2)
        self.assertEqual(len(polygons), 1)

    def test_edge_case_starty_endy_equal(self):
        polygons = calculate_polygons(0, 5, 10, 5, 2)
        self.assertEqual(len(polygons), 1)
