import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(find_angle(30, 60), 90)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(180, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(find_angle(0, 180), 180)
        self.assertEqual(find_angle(180, 0), 180)
        self.assertEqual(find_angle(90, 90), 0)
        self.assertEqual(find_angle(-30, 60), 90)
        self.assertEqual(find_angle(30, -60), 90)

    def test_negative_angles(self):
        self.assertEqual(find_angle(-30, -60), 90)
        self.assertEqual(find_angle(-90, -90), 0)
        self.assertEqual(find_angle(-180, 0), 180)
        self.assertEqual(find_angle(-180, 180), 0)
