import unittest
from mbpp_789_code import pi
from 789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter_polygon(10, 5), 50)

    def test_edge_case_zero_side(self):
        self.assertEqual(perimeter_polygon(0, 10), 0)

    def test_edge_case_zero_length(self):
        self.assertEqual(perimeter_polygon(10, 0), 0)

    def test_edge_case_pi_side(self):
        self.assertAlmostEqual(perimeter_polygon(pi, 1), 2 * pi)

    def test_edge_case_pi_length(self):
        self.assertAlmostEqual(perimeter_polygon(1, pi), 2 * pi)
