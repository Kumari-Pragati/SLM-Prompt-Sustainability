import unittest
from mbpp_356_code import find_angle

class TestFindAngle(unittest.TestCase):

    def test_zero_sum_degrees(self):
        self.assertEqual(find_angle(45, 45), 90)

    def test_sum_less_than_180_degrees(self):
        self.assertEqual(find_angle(30, 60), 90)

    def test_sum_greater_than_180_degrees(self):
        self.assertEqual(find_angle(200, 160), 20)

    def test_sum_equal_to_180_degrees(self):
        self.assertEqual(find_angle(180, 0), 0)

    def test_negative_angles(self):
        self.assertEqual(find_angle(-45, -30), 155)

    def test_one_argument_zero(self):
        with self.assertRaises(ValueError):
            find_angle(0, 45)

    def test_one_argument_negative(self):
        with self.assertRaises(ValueError):
            find_angle(-45, 30)
