import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):
    def test_typical_use_case(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(len(polygons), 3)

    def test_edge_case_startx_zero(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[0][0][0], 0)

    def test_edge_case_starty_zero(self):
        polygons = calculate_polygons(0, 0, 10, 10, 5)
        self.assertEqual(polygons[0][0][1], 0)

    def test_edge_case_endx_max(self):
        polygons = calculate_polygons(0, 0, 100, 100, 5)
        self.assertEqual(polygons[0][5][0], 95)

    def test_edge_case_endy_max(self):
        polygons = calculate_polygons(0, 0, 10, 100, 5)
        self.assertEqual(polygons[0][5][1], 95)

    def test_invalid_input_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, -5)

    def test_invalid_input_non_numeric_startx(self):
        with self.assertRaises(TypeError):
            calculate_polygons('a', 0, 10, 10, 5)

    def test_invalid_input_non_numeric_starty(self):
        with self.assertRaises(TypeError):
            calculate_polygons(0, 'a', 10, 10, 5)

    def test_invalid_input_non_numeric_endx(self):
        with self.assertRaises(TypeError):
            calculate_polygons(0, 0, 'a', 10, 5)

    def test_invalid_input_non_numeric_endy(self):
        with self.assertRaises(TypeError):
            calculate_polygons(0, 0, 10, 'a', 5)
