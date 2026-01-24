import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(5), 12.5)

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            area_pentagon(-5)

    def test_edge_case_zero_length(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_width(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_height(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_width(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_height(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_width_height(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_width_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_height_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_width_height(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_width_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_height_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_width_height_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_zero_length_width_height_radius(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)
