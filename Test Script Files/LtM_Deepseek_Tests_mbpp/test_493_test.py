import unittest
from mbpp_493_code import calculate_polygons

class TestCalculatePolygons(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(calculate_polygons(0, 0, 10, 10, 1), [(0, 1, 2, 3, 4, 5, 0, 1)])

    def test_edge_conditions(self):
        self.assertEqual(calculate_polygons(0, 0, 0, 0, 0), [])
        self.assertEqual(calculate_polygons(0, 0, 10, 10, 10), [(0, 10, 20, 30, 40, 50, 0, 10)])

    def test_boundary_conditions(self):
        self.assertEqual(calculate_polygons(-10, -10, 10, 10, 1), [(-10, 0, 10, 20, 30, 40, -10, 0)])
        self.assertEqual(calculate_polygons(0, 0, 1000000000, 1000000000, 1), [(0, 1, 2, 3, 4, 5, 0, 1)])

    def test_complex_cases(self):
        self.assertEqual(calculate_polygons(-10, -10, 10, 10, 2), [(-20, 2, 22, 24, 26, 28, -20, 2), (-10, 12, 14, 16, 18, 20, -10, 12)])
