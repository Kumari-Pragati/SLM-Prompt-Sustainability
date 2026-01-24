import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter_polygon(5, 3), 15)

    def test_edge_case_zero_side(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_edge_case_zero_side_and_length(self):
        self.assertEqual(perimeter_polygon(0, 0), 0)

    def test_edge_case_negative_side(self):
        self.assertEqual(perimeter_polygon(-5, 3), 15)

    def test_edge_case_negative_length(self):
        self.assertEqual(perimeter_polygon(5, -3), 15)

    def test_edge_case_negative_side_and_length(self):
        self.assertEqual(perimeter_polygon(-5, -3), 15)

    def test_edge_case_zero_side_and_negative_length(self):
        self.assertEqual(perimeter_polygon(0, -3), 0)

    def test_edge_case_zero_side_and_positive_length(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_edge_case_positive_side_and_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_edge_case_positive_side_and_negative_length(self):
        self.assertEqual(perimeter_polygon(5, -3), 15)

    def test_edge_case_positive_side_and_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 15)
