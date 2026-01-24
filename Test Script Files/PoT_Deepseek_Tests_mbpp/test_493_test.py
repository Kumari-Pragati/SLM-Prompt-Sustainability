import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_case(self):
        result = calculate_polygons(0, 0, 10, 10, 1)
        self.assertEqual(len(result), 100)

    def test_edge_case_small_radius(self):
        result = calculate_polygons(0, 0, 10, 10, 0.1)
        self.assertEqual(len(result), 10)

    def test_boundary_case_startx_equals_endx(self):
        result = calculate_polygons(0, 0, 0, 10, 1)
        self.assertEqual(len(result), 0)

    def test_boundary_case_starty_equals_endy(self):
        result = calculate_polygons(0, 0, 10, 0, 1)
        self.assertEqual(len(result), 0)

    def test_corner_case_negative_radius(self):
        with self.assertRaises(Exception):
            calculate_polygons(0, 0, 10, 10, -1)

    def test_corner_case_negative_coordinates(self):
        result = calculate_polygons(-1, -1, 1, 1, 1)
        self.assertEqual(len(result), 4)

    def test_corner_case_large_radius(self):
        result = calculate_polygons(0, 0, 1000, 1000, 1000)
        self.assertEqual(len(result), 100000)
