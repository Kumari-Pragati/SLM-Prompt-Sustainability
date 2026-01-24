import unittest
from mbpp_848_code import area_trapezium

class TestAreaTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_trapezium(5, 5, 3), 12.5)

    def test_edge_case_base1_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_trapezium(0, 5, 3)

    def test_edge_case_base2_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_trapezium(5, 0, 3)

    def test_edge_case_height_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_trapezium(5, 5, 0)

    def test_edge_case_base1_and_base2_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_trapezium(0, 0, 3)

    def test_edge_case_base1_and_base2_negative(self):
        with self.assertRaises(ValueError):
            area_trapezium(-5, -5, 3)

    def test_edge_case_height_negative(self):
        with self.assertRaises(ValueError):
            area_trapezium(5, 5, -3)
