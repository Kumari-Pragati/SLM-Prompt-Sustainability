import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(perimeter_polygon(2, 3), 6)

    def test_edge_case_zero_side(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(perimeter_polygon(2, 0), 0)

    def test_edge_case_negative_side(self):
        self.assertEqual(perimeter_polygon(-2, 3), 0)

    def test_edge_case_negative_length(self):
        self.assertEqual(perimeter_polygon(2, -3), 0)

    def test_complex_input(self):
        self.assertEqual(perimeter_polygon(pi, 2), 6.283185307179586)
