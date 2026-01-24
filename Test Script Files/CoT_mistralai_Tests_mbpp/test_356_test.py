import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_find_angle_normal(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(180, 0), 0)

    def test_find_angle_edge_cases(self):
        self.assertEqual(find_angle(0, 90), 90)
        self.assertEqual(find_angle(90, 180), 90)
        self.assertEqual(find_angle(180, 180), 0)
        self.assertEqual(find_angle(0, 0), 180)

    def test_find_angle_invalid_inputs(self):
        self.assertRaises(ValueError, find_angle, -10, 10)
        self.assertRaises(ValueError, find_angle, 10, -10)
        self.assertRaises(ValueError, find_angle, 361, 1)
        self.assertRaises(ValueError, find_angle, 1, 361)
        self.assertRaises(ValueError, find_angle, 361, 361)
