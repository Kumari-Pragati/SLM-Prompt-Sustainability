import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_polygon(3, 4), 12.0)

    def test_edge_case_s_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 4)

    def test_edge_case_l_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(3, 0)

    def test_edge_case_s_one(self):
        self.assertAlmostEqual(area_polygon(1, 4), 16.0)

    def test_edge_case_l_one(self):
        self.assertAlmostEqual(area_polygon(3, 1), 4.0)

    def test_edge_case_s_pi(self):
        self.assertAlmostEqual(area_polygon(pi, 4), 16.0)

    def test_edge_case_l_pi(self):
        self.assertAlmostEqual(area_polygon(3, pi), 4.0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            area_polygon('a', 4)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            area_polygon(3, 'a')
