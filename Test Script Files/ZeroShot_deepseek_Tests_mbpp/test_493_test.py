import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_calculate_polygons(self):
        # Test case 1: normal case
        polygons = calculate_polygons(0, 0, 10, 10, 1)
        self.assertEqual(len(polygons), 10)
        self.assertEqual(polygons[0], [(0, 1), (0, 3), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (0, 1)])

        # Test case 2: negative radius
        polygons = calculate_polygons(0, 0, 10, 10, -1)
        self.assertEqual(len(polygons), 0)

        # Test case 3: zero radius
        polygons = calculate_polygons(0, 0, 10, 10, 0)
        self.assertEqual(len(polygons), 0)

        # Test case 4: startx > endx
        polygons = calculate_polygons(10, 0, 0, 10, 1)
        self.assertEqual(len(polygons), 0)

        # Test case 5: starty > endy
        polygons = calculate_polygons(0, 10, 10, 0, 1)
        self.assertEqual(len(polygons), 0)

        # Test case 6: large radius
        polygons = calculate_polygons(0, 0, 100, 100, 1000)
        self.assertEqual(len(polygons), 100)
