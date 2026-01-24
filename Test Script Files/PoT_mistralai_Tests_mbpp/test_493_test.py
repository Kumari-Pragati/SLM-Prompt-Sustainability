import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(calculate_polygons(1, 1, 3, 3, 1), [
            [(2, 2), (2, 4), (3, 4), (3, 3), (2, 2)],
            [(2, 4), (3, 4), (3, 5), (2, 5), (2, 4)]
        ])

    def test_edge_case_small_radius(self):
        self.assertListEqual(calculate_polygons(1, 1, 3, 3, 0.5), [
            [(2, 2), (2, 2.5), (2.5, 2.5), (2.5, 2), (2, 2)]
        ])

    def test_edge_case_large_radius(self):
        self.assertListEqual(calculate_polygons(1, 1, 3, 3, 2), [
            [(1, 1), (1, 5), (3, 5), (3, 3), (1, 1)],
            [(1, 5), (3, 5), (3, 7), (1, 7), (1, 5)]
        ])

    def test_edge_case_collinear_points(self):
        self.assertListEqual(calculate_polygons(1, 1, 3, 2, 1), [
            [(2, 1), (2, 2), (3, 2), (3, 3), (2, 1)]
        ])

    def test_edge_case_vertical_line(self):
        self.assertListEqual(calculate_polygons(1, 1, 1, 3, 1), [
            [(0, 2), (0, 3), (1, 3), (1, 2), (0, 2)]
        ])

    def test_edge_case_horizontal_line(self):
        self.assertListEqual(calculate_polygons(1, 1, 3, 1, 1), [
            [(2, 0), (3, 0), (3, 1), (2, 1), (2, 0)]
        ])
