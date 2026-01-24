import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(find_angle(30, 60), 90)
        self.assertAlmostEqual(find_angle(45, 45), 90)
        self.assertAlmostEqual(find_angle(60, 30), 90)

    def test_edge_cases(self):
        self.assertAlmostEqual(find_angle(0, 0), 180)
        self.assertAlmostEqual(find_angle(0, 180), 0)
        self.assertAlmostEqual(find_angle(180, 0), 0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(find_angle(90, 90), 0)
        self.assertAlmostEqual(find_angle(90, 0), 90)
        self.assertAlmostEqual(find_angle(0, 90), 90)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            find_angle(200, 60)
        with self.assertRaises(Exception):
            find_angle(-30, 60)
        with self.assertRaises(Exception):
            find_angle(30, -60)
        with self.assertRaises(Exception):
            find_angle(30, 200)
