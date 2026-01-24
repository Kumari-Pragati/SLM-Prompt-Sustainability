import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_input(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(len(polygons), 5)

    def test_edge_case(self):
        polygons = calculate_polygons(0, 0, 5, 5, 5)
        self.assertEqual(len(polygons), 2)

    def test_boundary_case(self):
        polygons = calculate_polygons(0, 0, 10, 10, 0)
        self.assertEqual(len(polygons), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_polygons('a', 'b', 'c', 'd', 'e')

    def test_zero_radius(self):
        polygons = calculate_polygons(0, 0, 10, 10, 0)
        self.assertEqual(len(polygons), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, -5)
