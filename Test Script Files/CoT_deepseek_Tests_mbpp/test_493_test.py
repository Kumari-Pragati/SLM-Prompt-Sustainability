import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_typical_case(self):
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 10
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertIsInstance(polygons, list)
        self.assertTrue(all(isinstance(poly, list) for poly in polygons))
        self.assertTrue(all(len(poly) == 7 for poly in polygons))

    def test_edge_cases(self):
        # Test with zero radius
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 0
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertEqual(polygons, [])

        # Test with negative radius
        startx, starty, endx, endy, radius = 0, 0, 100, 100, -10
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertEqual(polygons, [])

        # Test with non-integer coordinates
        startx, starty, endx, endy, radius = 0.5, 0.5, 100.5, 100.5, 10
        polygons = calculate_polygons(startx, starty, endx, endy, radius)
        self.assertIsInstance(polygons, list)
        self.assertTrue(all(isinstance(poly, list) for poly in polygons))
        self.assertTrue(all(len(poly) == 7 for poly in polygons))

    def test_invalid_inputs(self):
        # Test with non-numeric coordinates
        startx, starty, endx, endy, radius = 'a', 'b', 'c', 'd', 'e'
        with self.assertRaises(TypeError):
            calculate_polygons(startx, starty, endx, endy, radius)

        # Test with non-numeric radius
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 'f'
        with self.assertRaises(TypeError):
            calculate_polygons(startx, starty, endx, endy, radius)

        # Test with radius as a negative string
        startx, starty, endx, endy, radius = 0, 0, 100, 100, '-10'
        with self.assertRaises(ValueError):
            calculate_polygons(startx, starty, endx, endy, radius)
