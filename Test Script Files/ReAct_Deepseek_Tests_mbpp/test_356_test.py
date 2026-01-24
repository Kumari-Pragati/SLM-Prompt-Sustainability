import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(find_angle(30, 60), 90)

    def test_edge_case_with_zero(self):
        self.assertAlmostEqual(find_angle(0, 0), 180)

    def test_edge_case_with_180(self):
        self.assertAlmostEqual(find_angle(180, 0), 0)

    def test_edge_case_with_90(self):
        self.assertAlmostEqual(find_angle(90, 0), 90)

    def test_edge_case_with_90_and_90(self):
        self.assertAlmostEqual(find_angle(90, 90), 0)

    def test_error_case_with_negative_values(self):
        with self.assertRaises(Exception):
            find_angle(-10, 20)

    def test_error_case_with_greater_than_180(self):
        with self.assertRaises(Exception):
            find_angle(200, 60)
