import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_find_angle(self):
        self.assertEqual(find_angle(60, 60), 60)
        self.assertEqual(find_angle(90, 30), 60)
        self.assertEqual(find_angle(45, 45), 90)
        self.assertEqual(find_angle(30, 90), 60)
        self.assertEqual(find_angle(0, 0), 180)
        self.assertEqual(find_angle(90, 0), 90)
        self.assertEqual(find_angle(0, 90), 90)
        self.assertEqual(find_angle(45, 135), 0)
        self.assertEqual(find_angle(135, 45), 0)
        self.assertEqual(find_angle(0, 180), 0)
        self.assertEqual(find_angle(180, 0), 0)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(0, 0), 180)
