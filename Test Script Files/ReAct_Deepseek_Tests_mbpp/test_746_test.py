import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sector_area(5, 90), 19.6349543, places=4)

    def test_typical_case_with_large_angle(self):
        self.assertAlmostEqual(sector_area(5, 360), 78.5398163, places=4)

    def test_edge_case_with_zero_radius(self):
        self.assertEqual(sector_area(0, 90), 0)

    def test_edge_case_with_zero_angle(self):
        self.assertEqual(sector_area(5, 0), 0)

    def test_edge_case_with_large_radius(self):
        self.assertAlmostEqual(sector_area(1000, 90), 7853.98163, places=4)

    def test_error_case_with_negative_radius(self):
        self.assertIsNone(sector_area(-5, 90))

    def test_error_case_with_negative_angle(self):
        self.assertIsNone(sector_area(5, -90))

    def test_error_case_with_large_angle(self):
        self.assertIsNone(sector_area(5, 361))
