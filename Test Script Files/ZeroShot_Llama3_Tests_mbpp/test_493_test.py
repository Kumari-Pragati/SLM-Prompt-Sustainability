import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_calculate_polygons(self):
        startx = 0
        starty = 0
        endx = 10
        endy = 10
        radius = 5
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertEqual(len(polygons), 3)
        self.assertEqual(len(polygons[0]), 7)
        self.assertEqual(polygons[0][0], (0, 5))
        self.assertEqual(polygons[0][1], (0, 10))
        self.assertEqual(polygons[0][2], (5, 10))
        self.assertEqual(polygons[0][3], (5, 5))
        self.assertEqual(polygons[0][4], (0, 5))
        self.assertEqual(polygons[0][5], (0, 10))
        self.assertEqual(polygons[0][6], (0, 5))

    def test_calculate_polygons_edge_case(self):
        startx = 0
        starty = 0
        endx = 5
        endy = 5
        radius = 5
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertEqual(len(polygons), 1)
        self.assertEqual(len(polygons[0]), 6)
        self.assertEqual(polygons[0][0], (0, 2.5))
        self.assertEqual(polygons[0][1], (0, 5))
        self.assertEqual(polygons[0][2], (2.5, 5))
        self.assertEqual(polygons[0][3], (2.5, 2.5))
        self.assertEqual(polygons[0][4], (0, 2.5))
        self.assertEqual(polygons[0][5], (0, 5))
