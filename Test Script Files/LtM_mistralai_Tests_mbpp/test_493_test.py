import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_simple_case(self):
        startx, starty, endx, endy, radius = 1, 1, 3, 3, 1
        expected = [
            [(2, 2), (2, 4), (3, 4), (3, 3), (2, 3), (2, 2)],
            [(2, 4), (3, 4), (3, 5), (2, 5), (2, 4)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected)

    def test_edge_case_min_radius(self):
        startx, starty, endx, endy, radius = 1, 1, 3, 3, 0
        expected = [
            [(2, 2), (2, 4), (3, 4), (3, 3), (2, 3), (2, 2)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected)

    def test_edge_case_max_radius(self):
        startx, starty, endx, endy, radius = 1, 1, 3, 3, 1000000
        expected = [
            [(2, 2), (2, 4), (3, 4), (3, 3), (2, 3), (2, 2)],
            [(2, 4), (3, 4), (3, 5), (2, 5), (2, 4)],
            [(3, 4), (4, 5), (4, 6), (3, 6), (3, 4)],
            [(4, 5), (5, 6), (5, 7), (4, 7), (4, 5)],
            [(3, 6), (4, 6), (4, 7), (3, 7), (3, 6)],
            [(4, 6), (5, 7), (5, 8), (4, 8), (4, 6)],
            [(5, 7), (6, 8), (6, 9), (5, 9), (5, 7)],
            [(6, 8), (7, 9), (7, 10), (6, 10), (6, 8)],
            [(7, 9), (8, 10), (8, 11), (7, 11), (7, 9)],
            [(8, 10), (9, 11), (9, 12), (8, 12), (8, 10)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected)

    def test_complex_case(self):
        startx, starty, endx, endy, radius = 1, 1, 5, 5, 2
        expected = [
            [(3, 3), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3)],
            [(3, 5), (4, 5), (4, 6), (3, 6), (3, 5)],
            [(4, 5), (5, 6), (5, 7), (4, 7), (4, 5)],
            [(4, 6), (5, 7), (5, 8), (4, 8), (4, 6)],
            [(5, 7), (6, 8), (6, 9), (5, 9), (5, 7)],
            [(5, 8), (6, 9), (6, 10), (5, 10), (5, 8)],
            [(6, 9), (7,