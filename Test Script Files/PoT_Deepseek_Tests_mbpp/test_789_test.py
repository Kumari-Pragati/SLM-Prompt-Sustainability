import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_polygon(5, 10), 50)

    def test_edge_case_zero_sides(self):
        self.assertEqual(perimeter_polygon(0, 10), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_boundary_case_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(-5, 10)

    def test_boundary_case_negative_length(self):
        with self.assertRaises(ValueError):
            perimeter_polygon(5, -10)

    def test_corner_case_large_numbers(self):
        self.assertEqual(perimeter_polygon(1000000, 1000000), 2000000000000)
