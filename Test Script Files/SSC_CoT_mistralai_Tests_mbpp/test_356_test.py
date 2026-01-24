import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(180 - 30, 180 - 60), 30)

    def test_edge_cases(self):
        self.assertEqual(find_angle(0, 180), 180)
        self.assertEqual(find_angle(180, 0), 180)
        self.assertEqual(find_angle(180, 180), 0)
        self.assertEqual(find_angle(-30, 60), 110)
        self.assertEqual(find_angle(30, -60), 110)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, find_angle, -181, 180)
        self.assertRaises(ValueError, find_angle, 181, -181)
        self.assertRaises(ValueError, find_angle, 180, 180)
        self.assertRaises(ValueError, find_angle, -360, 360)
        self.assertRaises(ValueError, find_angle, 360, -360)
