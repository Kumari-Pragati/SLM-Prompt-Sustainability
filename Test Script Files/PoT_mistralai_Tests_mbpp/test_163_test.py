import unittest
from mbpp_163_code import pi, tan
from 163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(3, 4), 3.770857560974936)
        self.assertAlmostEqual(area_polygon(4, 3), 12.566370614359172)

    def test_edge_case_sides(self):
        self.assertAlmostEqual(area_polygon(1, 1), 0.2617993877991494)
        self.assertAlmostEqual(area_polygon(2, 1), 1.047197551166557)

    def test_edge_case_sides_zero(self):
        self.assertAlmostEqual(area_polygon(1, 0), 0)
        self.assertAlmostEqual(area_polygon(0, 1), 0)

    def test_edge_case_sides_negative(self):
        self.assertAlmostEqual(area_polygon(-1, 1), -0.2617993877991494)
        self.assertAlmostEqual(area_polygon(1, -1), -1.047197551166557)

    def test_edge_case_sides_infinite(self):
        self.assertAlmostEqual(area_polygon(0.001, 1000000), 318.30988618379064)
        self.assertAlmostEqual(area_polygon(1000000, 0.001), 318.30988618379064)
