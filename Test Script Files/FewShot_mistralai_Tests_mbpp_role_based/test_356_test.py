import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):
    def test_sum_of_angles_less_than_180(self):
        self.assertEqual(find_angle(30, 120), 30)

    def test_sum_of_angles_equal_to_180(self):
        self.assertEqual(find_angle(80, 100), 0)

    def test_sum_of_angles_greater_than_180(self):
        self.assertEqual(find_angle(190, 50), -30)

    def test_negative_angles(self):
        self.assertEqual(find_angle(-30, -120), 150)

    def test_zero_angle(self):
        self.assertEqual(find_angle(0, 180), 0)
