import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(10, 90), 78.57142857142857)

    def test_edge_case_a_360(self):
        self.assertIsNone(sector_area(10, 360))

    def test_edge_case_a_0(self):
        self.assertIsNone(sector_area(10, 0))

    def test_edge_case_r_0(self):
        self.assertIsNone(sector_area(0, 90))

    def test_edge_case_a_negative(self):
        with self.assertRaises(ValueError):
            sector_area(10, -90)

    def test_edge_case_r_negative(self):
        with self.assertRaises(ValueError):
            sector_area(-10, 90)

    def test_edge_case_a_greater_than_360(self):
        self.assertIsNone(sector_area(10, 400))

    def test_edge_case_r_greater_than_100(self):
        self.assertAlmostEqual(sector_area(100, 90), 31415.92653589793)
