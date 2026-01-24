import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_simple_input(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(len(polygons), 2)

    def test_edge_case(self):
        polygons = calculate_polygons(-10, -10, 10, 10, 5)
        self.assertEqual(len(polygons), 2)

    def test_max_input(self):
        polygons = calculate_polygons(1000, 1000, 1100, 1100, 500)
        self.assertEqual(len(polygons), 2)

    def test_min_input(self):
        polygons = calculate_polygons(-1000, -1000, -900, -900, 500)
        self.assertEqual(len(polygons), 2)

    def test_zero_radius(self):
        polygons = calculate_polygons(0, 0, 10, 10, 0)
        self.assertEqual(len(polygons), 0)

    def test_negative_radius(self):
        polygons = calculate_polygons(0, 0, 10, 10, -5)
        self.assertEqual(len(polygons), 0)

    def test_non_integer_radius(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5.5)
        self.assertEqual(len(polygons), 2)

    def test_non_integer_coordinates(self):
        polygons = calculate_polygons(0.5, 0.5, 10.5, 10.5, 5)
        self.assertEqual(len(polygons), 2)
