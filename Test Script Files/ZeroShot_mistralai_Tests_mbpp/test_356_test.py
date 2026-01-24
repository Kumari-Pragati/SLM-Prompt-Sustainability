import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_find_angle_with_valid_angles(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(180, 0), 0)

    def test_find_angle_with_invalid_angles(self):
        self.assertRaises(ValueError, find_angle, -10, 10)
        self.assertRaises(ValueError, find_angle, 10, -10)
        self.assertRaises(ValueError, find_angle, 200, 50)
