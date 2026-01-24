import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_find_angle_positive_numbers(self):
        self.assertAlmostEqual(find_angle(30, 60), 90)
        self.assertAlmostEqual(find_angle(45, 45), 90)
        self.assertAlmostEqual(find_angle(60, 30), 90)

    def test_find_angle_negative_numbers(self):
        self.assertAlmostEqual(find_angle(-30, -60), 120)
        self.assertAlmostEqual(find_angle(-45, -45), 135)
        self.assertAlmostEqual(find_angle(-60, -30), 150)

    def test_find_angle_zero(self):
        self.assertAlmostEqual(find_angle(0, 0), 180)

    def test_find_angle_large_numbers(self):
        self.assertAlmostEqual(find_angle(179, 1), 1)
        self.assertAlmostEqual(find_angle(89, 91), 90)

    def test_find_angle_edge_cases(self):
        self.assertAlmostEqual(find_angle(90, 0), 90)
        self.assertAlmostEqual(find_angle(0, 90), 90)
        self.assertAlmostEqual(find_angle(180, 0), 0)
        self.assertAlmostEqual(find_angle(0, 180), 0)
