import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(5), 196.98479092281645)

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            area_pentagon(-5)

    def test_edge_case_zero_area(self):
        self.assertAlmostEqual(area_pentagon(0), 0)

    def test_edge_case_zero_input(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)
