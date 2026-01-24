import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_case(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(len(polygons), 5)

    def test_edge_case_startx_zero(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[0][0], 0)

    def test_edge_case_starty_zero(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[0][1], 0)

    def test_edge_case_endx_max(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[-1][0], 10)

    def test_edge_case_endy_max(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[-1][1], 10)

    def test_edge_case_radius_zero(self):
        polygons = calculate_polygons(0, 0, 10, 10, 0)
        self.assertEqual(len(polygons), 0)

    def test_edge_case_radius_negative(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, -5)

    def test_edge_case_startx_greater_than_endx(self):
        with self.assertRaises(ValueError):
            calculate_polygons(10, 0, 0, 10, 5)

    def test_edge_case_starty_greater_than_endy(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 10, 0, 0, 5)
