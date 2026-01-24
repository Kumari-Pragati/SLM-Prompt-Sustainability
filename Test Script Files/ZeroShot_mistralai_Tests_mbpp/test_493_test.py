import unittest
from mbpp_493_code import calculate_polygons
import math

class TestCalculatePolygons(unittest.TestCase):

    def test_calculate_polygons(self):
        # Test case 1: Basic functionality
        startx, starty, endx, endy, radius = 1, 1, 3, 3, 1
        expected_polygons = [
            [(1, 2), (2, 4), (3, 4), (3, 3), (2, 2), (1, 2)],
            [(2, 3), (3, 5), (4, 5), (4, 4), (3, 3), (2, 3)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected_polygons)

        # Test case 2: Edge case with start and end points on the circle
        startx, starty, endx, endy, radius = 2, 2, 2, 2.001, 1
        expected_polygons = [
            [(2, 2.995), (2.995, 3.99), (3.99, 3.99), (3.99, 2.995), (2.995, 2.995), (2, 2.995)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected_polygons)

        # Test case 3: Negative values
        startx, starty, endx, endy, radius = -1, -1, 1, 1, 1
        expected_polygons = [
            [(-2, -0.995), (-1.995, -0.99), (-1.99, -1.99), (-1.99, -1.995), (-1.995, -1.995), (-2, -1.995)],
            [(-1, -0.995), (-0.995, -0.99), (-0.99, -1.99), (-0.99, -1.995), (-0.995, -0.995), (-1, -0.995)]
        ]
        self.assertEqual(calculate_polygons(startx, starty, endx, endy, radius), expected_polygons)
