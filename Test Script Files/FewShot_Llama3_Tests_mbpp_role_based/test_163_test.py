import unittest
from mbpp_163_code import area_polygon

class TestAreaPolygon(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(area_polygon(3, 4), 6.123710095264458)

    def test_edge_case_s_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(0, 4)

    def test_edge_case_l_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_polygon(3, 0)

    def test_edge_case_s_one(self):
        self.assertAlmostEqual(area_polygon(1, 4), 4)

    def test_edge_case_l_large(self):
        self.assertAlmostEqual(area_polygon(3, 100), 1999.9999999999996)

    def test_invalid_input_type_s(self):
        with self.assertRaises(TypeError):
            area_polygon('a', 4)

    def test_invalid_input_type_l(self):
        with self.assertRaises(TypeError):
            area_polygon(3, 'b')
