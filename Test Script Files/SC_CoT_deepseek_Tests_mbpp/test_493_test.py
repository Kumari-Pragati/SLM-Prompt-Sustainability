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
        polygons = calculate_schemas(startx, starty, endx, endy, radius)
        self.assertEqual(polygons, [])

        # Test with negative radius
        startx, starty, endx, endy, radius = 0, 0, 100, 100, -10
        polygons = calculate_schemas(startx, starty, endx, endy, radius)
        self.assertEqual(polygons, [])

        # Test with radius greater than half of the width of the rectangle
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 101
        polygons = calculate_schemas(startx, starty, endx, endy, radius)
        self.assertEqual(polygons, [])

    def test_corner_cases(self):
        # Test with radius exactly half of the width of the rectangle
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 50
        polygons = calculate_schemas(startx, starty, endx, endy, radius)
        self.assertIsInstance(polygons, list)
        self.assertTrue(all(isinstance(poly, list) for poly in polygons))
        self.assertTrue(all(len(poly) == 7 for poly in polygons))

        # Test with radius exactly equal to the width of the rectangle
        startx, starty, endx, endy, radius = 0, 0, 100, 100, 100
        polygons = calculate_schemas(startx, starty, endx, endy, radius)
        self.assertIsInstance(polygons, list)
        self.assertTrue(all(isinstance(poly, list) for poly in polygons))
        self.assertTrue(all(len(poly) == 7 for poly in polygons))

    def test_invalid_inputs(self):
        # Test with non-numeric inputs
        startx, starty, endx, endy, radius = 'a', 'b', 'c', 'd', 'e'
        with self.assertRaises(TypeError):
            calculate_schemas(startx, starty, endx, endy, radius)

        # Test with non-numeric inputs
        startx, starty, endx, endy, radius = None, None, None, None, None
        with self.assertRaises(TypeError):
            calculate_schemas(startx, starty, endx, endy, radius)
