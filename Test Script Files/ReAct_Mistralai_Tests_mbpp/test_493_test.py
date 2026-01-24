import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_normal_case(self):
        result = calculate_polygons(0, 0, 10, 10, 5)
        expected = [
            [(0, 3.872983346207407), (3.872983346207407, 7.745966692414814),
             (7.745966692414814, 10, 10), (10, 7.745966692414814, 3.872983346207407),
             (10, 3.872983346207407), (0, 0)],
            [(3.872983346207407, 7.745966692414814), (7.745966692414814, 10),
             (10, 10), (10, 7.745966692414814), (7.745966692414814, 3.872983346207407),
             (3.872983346207407, 0)],
            ...
        ]
        self.assertEqual(result, expected)

    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_polygons(0, 0, 10, 10, -1)

    def test_start_end_points_coincide(self):
        result = calculate_polygons(0, 0, 0, 0, 5)
        self.assertEqual(result, [])

    def test_start_end_points_almost_coincide(self):
        epsilon = 0.001
        result = calculate_polygons(0, 0, 0.001, 0, 5)
        expected = [
            [(0, 3.872983346207407), (3.872983346207407, 7.745966692414814),
             (7.745966692414814, 10, 10), (10, 7.745966692414814),
             (10, 3.872983346207407), (0, 0)],
        ]
        self.assertListEqual(result, expected)

    def test_start_end_points_swapped(self):
        result = calculate_polygons(10, 10, 0, 0, 5)
        expected = [
            [(0, -3.872983346207407), (-3.872983346207407, -7.745966692414814),
             (-7.745966692414814, -10, -10), (-10, -7.745966692414814),
             (-10, -3.872983346207407), (0, 0)],
        ]
        self.assertListEqual(result, expected)

    def test_negative_coordinates(self):
        result = calculate_