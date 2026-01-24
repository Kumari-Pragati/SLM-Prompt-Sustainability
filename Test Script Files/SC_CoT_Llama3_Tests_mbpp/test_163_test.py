import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_input(self):
        self.assertAlmostEqual(area_polygon(4, 3), 6.0, places=2)

    def test_edge_case_s_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 3)

    def test_edge_case_l_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(4, 0)

    def test_edge_case_s_one(self):
        self.assertAlmostEqual(area_polygon(1, 3), 3.0, places=2)

    def test_edge_case_s_negative(self):
        with self.assertRaises(ValueError):
            area_polygon(-4, 3)

    def test_edge_case_l_negative(self):
        with self.assertRaises(ValueError):
            area_polygon(4, -3)

    def test_edge_case_s_and_l_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 0)

    def test_edge_case_s_and_l_negative(self):
        with self.assertRaises(ValueError):
            area_polygon(-4, -3)
