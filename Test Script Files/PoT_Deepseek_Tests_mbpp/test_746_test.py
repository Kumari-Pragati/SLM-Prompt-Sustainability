import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.634954354085742)

    def test_typical_case_2(self):
        self.assertAlmostEqual(sector_area(10, 180), 314.1592653589793)

    def test_edge_case_0_degrees(self):
        self.assertEqual(sector_area(5, 0), 0)

    def test_edge_case_360_degrees(self):
        self.assertIsNone(sector_area(5, 360))

    def test_edge_case_negative_degrees(self):
        self.assertIsNone(sector_area(5, -10))

    def test_corner_case_large_degrees(self):
        self.assertIsNone(sector_area(5, 361))

    def test_corner_case_large_radius(self):
        self.assertIsNone(sector_area(10000000000, 90))

    def test_corner_case_negative_radius(self):
        self.assertIsNone(sector_area(-5, 90))
