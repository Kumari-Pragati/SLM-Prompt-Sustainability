import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):
    def test_valid_input(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(len(polygons), 6)
        for poly in polygons:
            self.assertEqual(len(poly), 6)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, -5)

    def test_invalid_start_point(self):
        with self.assertRaises(ValueError):
            calculate_polygons(-1, 0, 10, 10, 5)

    def test_invalid_end_point(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, -1, 10, 10, 5)
