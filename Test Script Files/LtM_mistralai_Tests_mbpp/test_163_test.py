import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_simple_case(self):
        self.assertAlmostEqual(area_polygon(3, 4), 6.928203230275509)

    def test_edge_case_min(self):
        self.assertAlmostEqual(area_polygon(1, 1), 1.0)

    def test_edge_case_max(self):
        self.assertAlmostEqual(area_polygon(10000, 10000), 1000000000.0)

    def test_zero_sides(self):
        self.assertRaises(ValueError, area_polygon, 0, 1)

    def test_zero_length(self):
        self.assertRaises(ValueError, area_polygon, 1, 0)
