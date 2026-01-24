import unittest
from mbpp_789_code import pi
from 789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(perimeter_polygon(5, 3), 15 * 3)

    def test_edge_case_zero_side(self):
        self.assertEqual(perimeter_polygon(0, 3), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(perimeter_polygon(5, 0), 0)

    def test_edge_case_negative_side(self):
        self.assertEqual(perimeter_polygon(-5, 3), -15 * 3)

    def test_edge_case_negative_length(self):
        self.assertEqual(perimeter_polygon(5, -3), 15 * -3)

    def test_pi_radius_circle(self):
        self.assertAlmostEqual(perimeter_polygon(2 * pi, 1), 2 * pi * 1)
